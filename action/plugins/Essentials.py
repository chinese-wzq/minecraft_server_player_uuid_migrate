from .. import base
import os


def process(server_info: base.ServerInfo):
    userdata_config = os.path.join(server_info.server_path, "config", "Essentials")
    base.backup_file(userdata_config + server_info.new_uuid + ".yml", "Essentials", server_info)
    os.rename(userdata_config + server_info.old_uuid + ".yml", userdata_config + server_info.new_uuid + ".yml")
