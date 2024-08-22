import os
from . import base


def migrate_saves(server_info: base.ServerInfo):
    server_path = server_info.server_path
    old_uuid = server_info.old_uuid
    new_uuid = server_info.new_uuid
    if input(_("是否确认迁移playerdata？(y/n)")) == "y":
        # 1. 找到玩家数据文件夹
        player_data_path = os.path.join(server_path, "world", "playerdata")
        # 2. 找到玩家数据文件
        player_data_files = os.listdir(player_data_path)
        if os.path.exists(os.path.join(player_data_path, old_uuid + ".dat")):
            for file in player_data_files:
                if file == old_uuid + ".dat":
                    # 3. 备份已存在的新UUID的玩家数据文件
                    base.backup_file(os.path.join(player_data_path, new_uuid + ".dat"), "playerdata", server_info)
                    # 4. 将旧UUID的玩家数据文件覆盖到新UUID的玩家数据文件
                    os.rename(os.path.join(player_data_path, old_uuid + ".dat"),
                              os.path.join(player_data_path, new_uuid + ".dat"))
                    print(_("playerdata迁移成功"))
                    break
        else:
            print(_("需要迁移的playerdata不存在"))
    # =========================
    if input(_("是否确认迁移玩家成就数据？(y/n)")) == "y":
        # 1. 找到玩家成就数据文件夹
        player_advancements_path = os.path.join(server_path, "world", "advancements")
        # 2. 找到玩家成就数据文件
        player_advancements_files = os.listdir(player_advancements_path)
        if os.path.exists(os.path.join(player_advancements_path, old_uuid + ".json")):
            # 3. 备份已存在的新UUID的玩家成就数据文件
            base.backup_file(os.path.join(player_advancements_path, new_uuid + ".json"), "advancements", server_info)
            # 4. 将旧UUID的玩家成就数据文件覆盖到新UUID的玩家成就数据文件
            os.rename(os.path.join(player_advancements_path, old_uuid + ".json"),
                      os.path.join(player_advancements_path, new_uuid + ".json"))
            print(_("玩家成就数据迁移成功"))
        else:
            print(_("需要迁移的玩家成就数据不存在"))
    # =========================
    if input(_("是否确认迁移stats数据？(y/n)")) == "y":
        # 1. 找到状态数据文件夹
        player_stats_path = os.path.join(server_path, "world", "stats")
        if not os.path.exists(player_stats_path):
            print(_("未找到stats数据文件夹"))
            return
        # 2. 找到状态数据文件
        player_stats_files = os.listdir(player_stats_path)
        if os.path.exists(os.path.join(player_stats_path, old_uuid + ".json")):
            # 3. 备份已存在的新UUID的状态数据文件
            base.backup_file(os.path.join(player_stats_path, new_uuid + ".json"), "stats", server_info)
            # 4. 将旧UUID的状态数据文件覆盖到新UUID的状态数据文件
            os.rename(os.path.join(player_stats_path, old_uuid + ".json"),
                      os.path.join(player_stats_path, new_uuid + ".json"))
            print(_("stats数据迁移成功"))
        else:
            print(_("需要迁移的stats数据不存在"))
