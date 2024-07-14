from . import base
import json
import os


def migrate_usercache(server_info: base.ServerInfo):
    if input(_("是否迁移 usercache.json 文件？(y/n)")) != "y":
        return
    server_path = server_info.server_path
    old_uuid = server_info.old_uuid
    new_uuid = server_info.new_uuid
    usercache_path = os.path.join(server_path, "usercache.json")
    # 1. 备份愿文件
    base.backup_file(usercache_path, "usercache", server_info, True)
    with open(usercache_path, "r") as f:
        usercache = json.load(f)
    for user in usercache:
        if user["uuid"] == old_uuid:
            user["uuid"] = new_uuid
        if user["uuid"] == new_uuid:
            del user
    with open(usercache_path, "w") as f:
        json.dump(usercache, f)
    print(_("usercache.json 已迁移成功"))
