import os
import shutil


class ServerInfo:
    def __init__(self, server_path: str, old_uuid: str, new_uuid: str):
        self.server_path = server_path
        self.old_uuid = old_uuid
        self.new_uuid = new_uuid


def backup_file(path: str, note: str, server_info: ServerInfo, keep: bool = False):
    backup_path = os.path.join(server_info.server_path, "migrate_backup")
    if not os.path.exists(backup_path):
        os.mkdir(backup_path)
    shutil.copyfile(path, os.path.join(backup_path, f"{note}.{os.path.basename(path)}"))
    if not keep:
        os.remove(path)
    print(_("已将 %s 备份到 %s") % (path, os.path.join(backup_path, f"{note}.{os.path.basename(path)}")))
