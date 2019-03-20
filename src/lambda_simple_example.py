""" Just s simple testing function."""


def lambda_handler(event, context):
        """ The name of this sub must match the lambda handler,
        and the two parameters are required.
        """
        return event['n'] * 10

        # Return whatever you like.
        # return [
        #          {"context_function_name": context.function_name},
        #          {"event": event},
        #          {"test": "one", "result": "fail"},
        #          {"test": "two", "result": "fail"}
        #        ]
