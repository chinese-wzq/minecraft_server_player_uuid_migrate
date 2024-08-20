import action.base as base
import os


def process(server_info: base.ServerInfo):
    userdata_config = os.path.join(server_info.server_path, "plugins", "Essentials", "userdata")
    base.backup_file(os.path.join(userdata_config, server_info.new_uuid + ".yml"), "Essentials", server_info)
    os.rename(os.path.join(userdata_config, server_info.old_uuid + ".yml"),
              os.path.join(userdata_config, server_info.new_uuid + ".yml"))
