from .. import base
import os


def process(server_info: base.ServerInfo):
    waypoints_flood=os.path.join(server_info.server_path,"data-storage","waypoints")