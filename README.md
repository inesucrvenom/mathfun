# mathfun
Package with implementation of AWS Lambda functions 
which compute several mathematical functions:
- [Fibonacci](https://en.wikipedia.org/wiki/Fibonacci_number)
- [Ackermann](https://en.wikipedia.org/wiki/Ackermann_function)
- [Factorial](https://en.wikipedia.org/wiki/Factorial)

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
    + create AWS IAM role, I used full access one (not wise!)
- Deploy lambdas
```
ansible-playbook deploy_all_lambdas.yml
```
- Run with example data
```
python run_manually.py
```
  - To run with own data, just edit that file
- Be happy seeing the results :)

## Notes
- Tests are available as both local (testing logic) 
and lambda (seeing how big results you can get in short time)
- If you want to create own lambda:
  + filename starts with lambda eg `lambda_test_function`
  + name handler `lambda_handler`
  + put code into `src` folder
  + deploy and run as previously described
  
  Works only for single-file lambdas.