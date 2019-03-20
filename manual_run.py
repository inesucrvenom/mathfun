"""Invoke manually specific lambda function

initial inspiration by:
http://blog.cesarcd.com/2017/07/sample-aws-lambda-client-written-in.html
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lambda.html#Lambda.Client.invoke
"""

import boto3
import json


def invoke_lambda(lambda_name: str, parameters: json) -> json:
    """Call lambda on AWS, return json file from its returned value."""
    client = boto3.client('lambda')

    response = client.invoke(
        FunctionName=lambda_name,
        LogType='Tail',
        InvocationType='RequestResponse',
        Payload=parameters,
    )

    # get human readable Payload which is <botocore.response.StreamingBody>
    response_json = json.loads(response['Payload'].read().decode("utf-8"))
    return response_json


def create_parameters(values: dict) -> json:
    """Create json for sending parameters to Lambda"""
    return json.dumps(values)


# todo: I'm not sure if this function print + call could be split better
def print_result(function_name: str, parameters: dict):
    """Print the result of invoked lambda in a human readable form.

    Arguments:
    parameters : dictionary {'n': value, 'm': value...}
        Label values so lambda can access them by name.

    Each lambda takes care of validating input.
    """
    result = invoke_lambda(function_name, create_parameters(parameters))
    call_parameters = tuple(parameters.values())
    print("{}{} = {}".format(function_name, call_parameters, result))


def run_all():
    """Create own lambda invocations"""
    print_result('lambda_simple_test', {'n': 33, 'm': 64, 'a': 14})
#    print_result('lambda_fibonacci_recursion', {'n': 5})


if __name__ == '__main__':
    run_all()
