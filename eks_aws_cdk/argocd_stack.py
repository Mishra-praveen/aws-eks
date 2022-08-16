from argparse import Namespace
from ensurepip import version
from multiprocessing.connection import wait
from multiprocessing.sharedctypes import Value
from optparse import Values
from platform import release
from sys import api_version
from aws_cdk import (
    # Duration,
    Stack,
    aws_s3 as s3,
    RemovalPolicy,
    aws_eks as eks,
    CfnOutput
)
from constructs import Construct

class ArgoCD(Stack):

    def __init__(self, scope: Construct, construct_id: str, cluster, config, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        
        argocd = cluster.add_helm_chart("ArgoCD", 
            chart=config.chart_name,
            repository=config.chart_repo,
            release="argocd",
            namespace="argocd",
            wait=True,
            values = {
                "server": {
                    "service": {
                        "type": "LoadBalancer"
                    },
                }
                
            }
        
        )

        CfnOutput(
            self,
            "AlbUrl",
            value=cluster.get_service_load_balancer_address(
                service_name = "argocd-server",
                namespace="argocd"
            )
        )
