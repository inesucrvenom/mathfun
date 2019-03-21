""" Generic call for lambda functions in src/

Each lambda has to take care of its own validation.
Each lambda returns either function int value or error message.
Check obligatory parameters for each lambda before calling it.
"""

import boto3
import json


def invoke_lambda(lambda_name: str, parameters: dict) -> (int, int):
    """Call lambda on AWS with given parameters.
    Return evaluation result as int.

    Errors include message from the lambda, for improving UX.
    - TypeError and ValueError from invoked lambda, propagate.
    - raise TypeError if result isn't already explained by lambda result.
    - RuntimeError for timeout and similar errors that come without type.
    - re-raise Exception for all other cases.
    """
    client = boto3.client('lambda')

    response = client.invoke(
        FunctionName=lambda_name,
        LogType='Tail',
        InvocationType='RequestResponse',
        Payload=json.dumps(parameters),
    )

    # extract human readable Payload of type <botocore.response.StreamingBody>
    result_json = json.loads(response['Payload'].read().decode("utf-8"))

    try:
        result_value = int(result_json)

    # distinguish and propagate exact errors from lambda
    # to filter out invalid user input from other errors
    except TypeError as type_err:
        error_message = result_json["errorMessage"]
        try:
            type = result_json["errorType"]
        except KeyError:
            # e.g. timeout
            raise RuntimeError(error_message)
        else:
            # lambda invalid input
            if type == "TypeError":
                raise TypeError(error_message) from type_err
            elif type == "ValueError":
                raise ValueError(error_message) from type_err
            else:
                raise Exception(error_message) from type_err
    except Exception as unk_err:
        raise Exception(str(result_json)) from unk_err

    else:
        return result_value


def show_result(function_name: str, parameters: dict) -> str:
    """Return the result of invoked lambda in a human readable form.
    Return reason if not computable, based on what lambda sent.

    Arguments:
    parameters : dictionary
        Parameters as requested by each lambda
    """
    message = "\n{}{} ".format(function_name, tuple(parameters.values()))

    try:
        result = invoke_lambda(function_name, parameters)
    except Exception as e:
        message = message + "is not computable\n" + str(e)
    else:
        message = message + "= {}".format(result)

    return message
