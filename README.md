# mathfun
Package with implementation of AWS Lambda functions 
which compute several mathematical functions:
- [Fibonacci](https://en.wikipedia.org/wiki/Fibonacci_number) R+B
- [Ackermann](https://en.wikipedia.org/wiki/Ackermann_function)
- [Factorial](https://en.wikipedia.org/wiki/Factorial)

Some are in recursive version only (R), others have better version (B) as well.

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
`source ./path_to_env/bin/activate`
- Get this package - unpack zip / pull from github
- Setup your AWS credentials and region with `aws configure`
  + Open AWS account if you don't have it
  + Get key for programmatic access 
  (eg [check here](https://hackernoon.com/creating-serverless-functions-with-python-and-aws-lambda-901d202d45dc) 
- Deploy lambdas
```
ansible-playbook deploy_all_lambdas.yml
```

## Usage
- Run with example data
```
python manual_run.py
```
- To run with own data, just edit that file

- Available tests:
  - local - main purpose was testing logic 
  - lambda - seeing responses and being able to evaluate big cases
    + don't forget to be online and deploy lambdas before testing

- If you want to create own lambda:
  + filename starts with lambda eg: `lambda_test_function`
  + name handler precisely: `lambda_handler`
  + put code into `src` folder
  + deploy and run as previously described
  + **Note:** Works only for single-file lambdas. For now.

Enjoy the results :)

# Note
In lambda tests something from boto3 throws warning in the console:
`ResourceWarning: unclosed <ssl.SSLSocket...`

It's still [open issue](https://github.com/boto/boto3/issues/454) 
why that warning comes. Seems that it can be safely ignored.
