from diagrams import Diagram
from diagrams.alibabacloud.network import SLB
from diagrams.alibabacloud.compute import ECS
from diagrams.alibabacloud.database import RDS

with Diagram("Web Service", show=False):
    SLB("lb") >> ECS("web") >> RDS("userdb")