# AWS CDK Python Projects

This repository contains multiple **AWS CDK (Cloud Development Kit)** projects written in Python.  
Each project demonstrates how to provision and manage AWS resources using Infrastructure as Code (IaC).

---

## 📌 Prerequisites

Before running any project, ensure you have the following installed:

- [Python 3.9+](https://www.python.org/downloads/)
- [Node.js (LTS)](https://nodejs.org/en/download/)
- [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) (configured with your credentials)
- [AWS CDK](https://docs.aws.amazon.com/cdk/v2/guide/getting_started.html)

```bash
npm install -g aws-cdk
```

## 📂 Project Structure
Each project is contained within its own directory, with the following structure:

```project_name/
├── .venv/                # Virtual environment directory   
├── cdk.json              # CDK configuration file
├── requirements.txt      # Python dependencies
├── setup.py              # Python package configuration
├── app.py                # CDK application entry point
├── README.md             # Project documentation
└── src/                  # Source code for the CDK stack
    └── my_stack.py        # CDK stack definition
```

CDK/
│── l1_construct/ # Example using L1 Constructs (low-level Cfn resources)

│── l2_construct/ # Example using L2 Constructs (higher-level CDK abstractions)

│── l3_construct/ # Example using L3 Constructs (patterns)

│── lambda/ # Example Lambda function deployment with CDK

│── multistack/ # Example of multiple stacks in a CDK app

│── s3bucket/ # Example creating an S3 bucket

│── s3bucket_lambda/ # Example S3 bucket and Lambda integration

│── string-or-numbers-step-function/ # Example Step Function to check if input is string or number

│── README.md # Documentation

## Commands to Get Started
### Create a Virtual Environment
To create a virtual environment for your project, run the following command in your project directory:
```bash 
python -m venv .venv
```
### Activate the Virtual Environment
- On **MacOS/Linux**:
```bash
source .venv/bin/activate
```
- On **Windows**:
```bash
.venv\Scripts\activate.bat
```
### Install Dependencies
After activating the virtual environment, install the required dependencies:
```bash
pip install -r requirements.txt
```
### Connect to AWS Account
Ensure your AWS CLI is configured with the correct credentials and region. You can check your configuration with:
```bash
aws configure
```

### Synthesize the CloudFormation Template
To generate the CloudFormation template for your CDK application, run:
```bash
cdk synth   
```         
### Deploy the Stack
To deploy your CDK stack to your AWS account, use:
```bash
cdk deploy
```
### Add Additional Dependencies
To add more dependencies, modify the `setup.py` file and run:
```bash
pip install -r requirements.txt
```
### Useful Commands
- `cdk ls`          - List all stacks in the app
- `cdk synth`       - Emit the synthesized CloudFormation template
- `cdk deploy`      - Deploy this stack to your default AWS account/region
- `cdk diff`        - Compare deployed stack with current state
- `cdk docs`        - Open CDK documentation
