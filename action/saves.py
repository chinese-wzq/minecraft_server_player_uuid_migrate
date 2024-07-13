import os
from . import base


def migrate_saves(server_info: base.ServerInfo):
    server_path = server_info.server_path
    old_uuid = server_info.old_uuid
    new_uuid = server_info.new_uuid
    # 1. 找到玩家数据文件夹
    player_data_path = os.path.join(server_path, "world", "playerdata")
    if not os.path.exists(player_data_path):
        print(_("未找到玩家数据文件夹"))
        return
    # 2. 找到玩家数据文件
    player_data_files = os.listdir(player_data_path)
    for file in player_data_files:
        if file == old_uuid + ".dat":
            # 3. 备份已存在的新UUID的玩家数据文件
            base.backup_file(os.path.join(player_data_path, old_uuid + ".dat"), "playerdata", server_info)
            # 4. 将旧UUID的玩家数据文件覆盖到新UUID的玩家数据文件
            os.rename(os.path.join(player_data_path, old_uuid + ".dat"),
                      os.path.join(player_data_path, new_uuid + ".dat"))
            print(_("玩家数据迁移成功"))
            break
    # =========================
    # 1. 找到玩家成就数据文件夹
    player_advancements_path = os.path.join(server_path, "world", "advancements")
    if not os.path.exists(player_advancements_path):
        print(_("未找到玩家成就数据文件夹"))
        return
    # 2. 找到玩家成就数据文件
    player_advancements_files = os.listdir(player_advancements_path)
    for file in player_advancements_files:
        if file == old_uuid + ".json":
            # 3. 备份已存在的新UUID的玩家成就数据文件
            base.backup_file(os.path.join(player_advancements_path, old_uuid + ".json"), "advancements", server_info)
            # 4. 将旧UUID的玩家成就数据文件覆盖到新UUID的玩家成就数据文件
            os.rename(os.path.join(player_advancements_path, old_uuid + ".json"),
                      os.path.join(player_advancements_path, new_uuid + ".json"))
            print(_("玩家成就数据迁移成功"))
            break
    # =========================
    # 1. 找到状态数据文件夹
    player_stats_path = os.path.join(server_path, "world", "stats")
    if not os.path.exists(player_stats_path):
        print(_("未找到状态数据文件夹"))
        return
    # 2. 找到状态数据文件
    player_stats_files = os.listdir(player_stats_path)
    for file in player_stats_files:
        if file == old_uuid + ".json":
            # 3. 备份已存在的新UUID的状态数据文件
            base.backup_file(os.path.join(player_stats_path, old_uuid + ".json"), "stats", server_info)
            # 4. 将旧UUID的状态数据文件覆盖到新UUID的状态数据文件
            os.rename(os.path.join(player_stats_path, old_uuid + ".json"),
                      os.path.join(player_stats_path, new_uuid + ".json"))
            print(_("状态数据迁移成功"))
            break
    # =========================
    print(_("玩家存档数据已迁移完成"))
