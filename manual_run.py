"""Invoke manually specific lambda function

initial inspiration by:
http://blog.cesarcd.com/2017/07/sample-aws-lambda-client-written-in.html
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lambda.html#Lambda.Client.invoke

"""

import boto3
import json


def invoke_lambda(lambda_name: str, params: json) -> json:
    """Call lambda function by name, send given parameters.
    Return json file from lambda's returned value
    """
    client = boto3.client('lambda')

    response = client.invoke(
        FunctionName=lambda_name,
        LogType='Tail',
        InvocationType='RequestResponse',
        Payload=params,
    )

    # get human readable Payload which is <botocore.response.StreamingBody>
    response_json = json.loads(response['Payload'].read().decode("utf-8"))
    return response_json


def create_params(values: dict) -> json:
    """Create json for sending parameters to lambda"""
    return json.dumps(values)


def print_result(function_name: str, param: dict):
    """Call lambda with given name, send her parameters given in args
    as dict {'n': value, 'm': value...}
    Each lambda takes care of validating input
    """
    result = invoke_lambda(function_name, create_params(param))
    params = tuple(param.values())
    print("{}{} = {}".format(function_name, params, result))


def run_all():
    """Create own lambda invocations"""
    print_result('lambda_simple_test', {'n': 33, 'm': 64, 'a': 14})
#    print_result('lambda_fibonacci_recursion', {'n': 5})


if __name__ == '__main__':
    run_all()
