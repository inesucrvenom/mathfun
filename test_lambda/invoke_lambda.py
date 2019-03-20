"""Invoke specific lambda function

initial inspiration by:
http://blog.cesarcd.com/2017/07/sample-aws-lambda-client-written-in.html
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lambda.html#Lambda.Client.invoke
"""

import boto3
import json


def invoke_lambda(lambda_name: str, parameters: json) -> (int, int):
    """Call lambda on AWS.

    Return
    (result_json, result_status) : (int, int)
        (value of evaluation, http response code)

    Each lambda takes care of its parameters and validation.

    Raise TypeError exception if json format changes.
    Propagates TypeError and ValueError from invoked lambda.
    """
    client = boto3.client('lambda')

    response = client.invoke(
        FunctionName=lambda_name,
        LogType='Tail',
        InvocationType='RequestResponse',
        Payload=parameters,
    )

    # defense from AWS changes + correct propagation of lambda's exceptions
    try:
        result_status = int(response['StatusCode'])
        # extract human readable Payload which is <botocore.response.StreamingBody>
        result_json = json.loads(response['Payload'].read().decode("utf-8"))

    except TypeError as e:
        raise TypeError("AWS response changed") from e

    else:
        # check if lambda sent some message instead of just value
        if type(result_json) != int:
            if result_json["errorType"] == "TypeError":
                raise TypeError(result_json["errorMessage"])
            elif result_json["errorType"] == "ValueError":
                raise ValueError(result_json["errorMessage"])
            else:
                raise TypeError("AWS response changed")
        else:
            result_value = int(result_json)
            return result_value, result_status


def create_parameters(values: dict) -> json:
    """Create json for sending parameters to Lambda"""
    return json.dumps(values)


def format_result(function_name: str, parameters: dict) -> str:
    """Return the result of invoked lambda in a human readable form
    when http response was 200 = OK.

    Arguments:
    parameters : dictionary {'n': value, 'm': value...}
        Label values so lambda can access them by name.
    """
    try:
        result, status = invoke_lambda(function_name, create_parameters(parameters))
    except TypeError as e:
        raise e
    else:
        # todo: maybe we want to allow all between 200 and 299?
        if status == 200:
            call_parameters = tuple(parameters.values())
            return "{}{} = {}".format(function_name, call_parameters, result)
        else:
            return "Error, check https://httpstatuses.com/{} for more info".format(status)
