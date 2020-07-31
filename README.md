![logo](repo-code.png)

# mathfun

Package with implementation of a few functions using AWS Lambda:
- [Fibonacci](https://en.wikipedia.org/wiki/Fibonacci_number) (x2)
- [Ackermann](https://en.wikipedia.org/wiki/Ackermann_function)
- [Factorial](https://en.wikipedia.org/wiki/Factorial) (x2)

All are implemented for non-negative integers.


## Dependencies

Recommended usage is to install virtual environment
and put in it whatever packages you need, not to disturb your system.

I've installed some packages system-wide and some in venv
(mostly those I've installed with pip).

- python >= 3.6
- pip
- virtual environment
- AWS CLI
- boto3 (maybe also botocore and boto if they're not automatically included)
- ansible

## Fedora example installation and deploy

- Install
```
dnf install python
dnf install pip
pip install virtualenv
pip3 install awscli --upgrade --user
pip install boto3
pip install botocore
pip install ansible
```
- Activate your venv if you're using it
```
$ source ./path_to_env/bin/activate
```
- Get this package & unpack zip OR pull from github
- Setup your AWS credentials and region with `aws configure`
  + Open AWS account if you don't have it
  + Get key for programmatic access
  (eg [check here](https://hackernoon.com/creating-serverless-functions-with-python-and-aws-lambda-901d202d45dc))
- Deploy lambdas
```
$ ansible-playbook deploy_all_lambdas.yml
```

## Usage
#### Run with example data

```
$ python manual_run.py
```

#### Run with own data
Just edit file `manual_run.py`

#### Tests
- type local - mainly to test logic, exception handling and running time
- type lambda - to verify logic, test lambda exception handling, evaluate
 big index cases
  + don't forget to be online and deploy lambdas before testing

#### Requirements for creating own lambda
- Filename must start with lambda eg: `lambda_test_function`
- Name handler hast to be: `lambda_handler`
- Put code into `src` folder
- Deploy and run as previously described
- **Note:** Works only for single-file lambdas. For now.


## Dashboard for comparison of max running time
Provided config files:
- `dashboard/cloudwatch_widget_upto500ms.json`
  -> comparison of all mentioned lambda versions, with cap on 500ms runtime.
- `dashboard/cloudwatch_widget_uptoMax.json`
  -> comparison for the same functions, with cap at max allowed runtime

In Cloudwatch console
- in dashboards > create dashboard > add widget
- pick 'line' > configure
- in tab 'Source' > paste content of the provided config file
- click update > create widget


In the same console, detailed analysing of logs is also possible.

## Note
In lambda tests something from boto3 throws this warning in the console:
`ResourceWarning: unclosed <ssl.SSLSocket...`

It's still [open issue](https://github.com/boto/boto3/issues/454)
why that warning happens, but it seems like it can be safely ignored.

## Decisions & thoughts
Post about background thoughts read [here](https://inesucrvenom.github.io/2019/03/aws-lambda-mathfun.html)

## Licence
**Tl;dr: Learn from here, don't present materials as yours.**

Published under [MIT licence](LICENCE)

![logo](repo-code.png)
