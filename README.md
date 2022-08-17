
# Welcome to your AWS-EKS-CDK Python project!

This code can be used to setup an EKS cluster using CDK development with Python.

To manually create a virtualenv on MacOS and Linux:

```
$ python3 -m venv .venv
```

After the init process completes and the virtualenv is created, you can use the following
step to activate your virtualenv.

```
$ source .venv/bin/activate
```

If you are a Windows platform, you would activate the virtualenv like this:

```
% .venv\Scripts\activate.bat
```

Once the virtualenv is activated, you can install the required dependencies.

```
$ pip install -r requirements.txt
```

At this point you can now synthesize the CloudFormation template for this code.

```
$ cdk synth --all --profile my-profile
```

To add additional dependencies, for example other CDK libraries, just add
them to your `setup.py` file and rerun the `pip install -r requirements.txt`
command.

## Useful commands

 * `cdk ls`          list all stacks in the app
 * `cdk synth EksStackdev --profile my-profile`       emits the synthesized CloudFormation template
 * `cdk deploy EksStackdev --profile my-profile`      deploy this stack to your default AWS account/region


* `cdk deploy --all --profile my-profile`          Deploy all stack at once
Enjoy!

