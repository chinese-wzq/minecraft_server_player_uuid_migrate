import action.base as base
import os
import sqlite3


def process(server_info: base.ServerInfo):
    slimefun_folder = os.path.join(server_info.server_path, "data-storage", "Slimefun")
    # 迁移waypoints文件
    waypoints_folder = os.path.join(slimefun_folder, "waypoints")
    base.backup_file(os.path.join(waypoints_folder, server_info.new_uuid + ".yml"), "Slimefun waypoints", server_info)
    os.rename(os.path.join(waypoints_folder, server_info.old_uuid + ".yml"),
              os.path.join(waypoints_folder, server_info.new_uuid + ".yml"))
    # 迁移profile.db文件
    db_file = os.path.join(slimefun_folder, "profile.db")
    base.backup_file(db_file, "Slimefun profile.db", server_info, True)
    con = sqlite3.connect(db_file)
    cur = con.cursor()
    # 迁移player_backpack表
    cur.execute("UPDATE player_backpack SET p_uuid=? WHERE p_uuid=?", (server_info.new_uuid, server_info.old_uuid))
    # 迁移player_research表（合并）
    # 先删除那些p_uuid为old_uuid且存在相同research_id的p_uuid为new_uuid的记录
    cur.execute('''
    DELETE FROM player_research
    WHERE p_uuid = ? AND EXISTS (
        SELECT 1 FROM player_research pr2
        WHERE pr2.research_id = player_research.research_id
        AND pr2.p_uuid = ?
    )''', (server_info.old_uuid, server_info.new_uuid))
    # 更新存留下来的p_uuid为old_uuid的记录
    cur.execute('''
    UPDATE player_research
    SET p_uuid = ?
    WHERE p_uuid = ?
    ''', (server_info.new_uuid, server_info.old_uuid))
    con.commit()
    con.close()
