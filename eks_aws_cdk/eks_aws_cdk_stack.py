from ensurepip import version
from sys import api_version
from aws_cdk import (
    # Duration,
    Stack,
    aws_eks as eks,
    aws_iam as iam,
    aws_s3 as s3,
    aws_ec2 as ec2
)
from constructs import Construct

class EksAwsCdkStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, config, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        ## Create an EKS cluster
        self.cluster = eks.Cluster(
            self,
            "EKSCluster",
            default_capacity_instance=ec2.InstanceType.of(ec2.InstanceClass.T3, ec2.InstanceSize.SMALL),
            version=eks.KubernetesVersion.V1_21,
            default_capacity_type=eks.DefaultCapacityType.EC2,
            alb_controller=eks.AlbControllerOptions(
                version=eks.AlbControllerVersion.V2_4_1
            ),
            cluster_name=config.env + "-cluster",
        )




