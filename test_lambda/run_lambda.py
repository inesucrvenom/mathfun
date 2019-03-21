""" Generic call for lambda functions in src/
Implement custom exception for better UI.

Each lambda has to take care of its own validation.
Each lambda returns either function int value or error message.
Check obligatory parameters for each lambda before calling it.
"""

import boto3
import json


def invoke_lambda(lambda_name: str, parameters: dict) -> (int, int):
    """Call lambda on AWS with given parameters.
    Return evaluation result as int.

    Propagate TypeError and ValueError from invoked lambda.
    Raise TypeError if result isn't already explained by lambda result.
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

    except TypeError as unspecified:
        # propagate exact error message sent by lambda
        if result_json["errorType"] == "TypeError":
            raise TypeError(result_json["errorMessage"]) from unspecified
        elif result_json["errorType"] == "ValueError":
            raise ValueError(result_json["errorMessage"]) from unspecified
        else:
            raise Exception(result_json) from unspecified

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
