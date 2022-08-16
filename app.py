#!/usr/bin/env python3
from distutils.command.config import config
import os
from omegaconf import OmegaConf
import aws_cdk as cdk

from eks_aws_cdk.eks_aws_cdk_stack import EksAwsCdkStack
from eks_aws_cdk.argocd_stack import ArgoCD
deploy_env = "dev"
conf = OmegaConf.load("{0}.yaml".format(deploy_env))
env_conf = cdk.Environment(account=conf.aws.account, region=conf.aws.region)
app = cdk.App()
ClusterStack = EksAwsCdkStack(
    app, 
    "EksStack{0}".format(conf.env), 
    stack_name = "EksStack", 
    config=conf, 
    env=env_conf, 
    tags = {
        "Environment": conf.env
    },
    description="Creates an EKS stack with associated resources"
)
ArgocdStack = ArgoCD(
    app, 
    "ArgocdStack{0}".format(conf.env), 
    stack_name = "ArogCDStack", 
    cluster=ClusterStack.cluster,
    tags = {
        "Environment": conf.env
    }, 
    config=conf, 
    env=env_conf, 
    description="Deploys ArgoCD helm chart on the cluster"
)
ArgocdStack.add_dependency(ClusterStack)
app.synth()
