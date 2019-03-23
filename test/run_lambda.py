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
    - get TypeError and ValueError from invoked lambda
    - get Exception when result isn't already explained by lambda result.
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
    except TypeError as err_json_not_int:
        distinguish_user_errors_from_others(result_json, err_json_not_int)
    except Exception as err_unknown:
        raise Exception(str(result_json)) from err_unknown
    else:
        return result_value


def distinguish_user_errors_from_others(result_json, err_json_not_int):
    """ Propagate exact errors based on type field, if it's available.
    Filtering out invalid user input from other errors.

    - Propagate TypeError and ValueError from invoked lambda
    - Raise Exception when no type found.
    """
    error_message = result_json["errorMessage"]
    try:
        err_type_user_input = result_json["errorType"]
    except Exception as err_unknown:
        raise Exception(error_message) from err_unknown
    else:
        # Distinguish invalid user input in lambda.
        if err_type_user_input == "TypeError":
            raise TypeError(error_message) from err_json_not_int
        elif err_type_user_input == "ValueError":
            raise ValueError(error_message) from err_json_not_int
        else:
            raise Exception(error_message) from err_json_not_int


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
        message += "is not computable\n" + str(e)
    else:
        message += "= {}".format(result)

    return message
