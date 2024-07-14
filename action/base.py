import os
import shutil


class ServerInfo:
    def __init__(self, server_path: str, old_uuid: str, new_uuid: str):
        self.server_path = server_path
        self.old_uuid = old_uuid
        self.new_uuid = new_uuid


def backup_file(path: str, note: str, server_info: ServerInfo, keep: bool = False):
    """
    一个备份文件的函数，备份到 server_path/migrate_backup 文件夹下
    如果要备份的文件不存在也不会报错
    :param path:
    :param note:
    :param server_info:
    :param keep:
    :return:
    """
    backup_path = os.path.join(server_info.server_path, "migrate_backup")
    if not os.path.exists(backup_path):
        os.mkdir(backup_path)
    for i in range(1, 100):
        if not os.path.exists(os.path.join(backup_path, f"{note}_{i}.{os.path.basename(path)}")):
            note = f"{note}_{i}"
            break
    try:
        shutil.copyfile(path, os.path.join(backup_path, f"{note}.{os.path.basename(path)}"))
    except FileNotFoundError:
        print(_("要备份的文件 %s 不存在，忽略之") % path)
        return
    if not keep:
        os.remove(path)
    print(_("已将 %s 备份到 %s") % (path, os.path.join(backup_path, f"{note}.{os.path.basename(path)}")))
