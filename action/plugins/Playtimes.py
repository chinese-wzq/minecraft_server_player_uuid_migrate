from .. import base
import os


def process(server_info: base.ServerInfo):
    data_file = os.path.join(server_info.server_path, "plugins", "Playtimes", "data.yml")
    base.backup_file(data_file, "Playtimes", server_info, True)
    with open(data_file, "r") as f:
        data = f.read()
    # 删除包含new_uuid的行
    data = '\n'.join([line for line in data.split('\n') if server_info.new_uuid not in line])
    # 将所有old_uuid替换为new_uuid
    data = data.replace(server_info.old_uuid, server_info.new_uuid)
    with open(data_file, "w") as f:
        f.write(data)
