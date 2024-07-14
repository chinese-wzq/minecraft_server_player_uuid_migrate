from .. import base
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
    cur.execute("UPDATE player_backpack SET p_uuid=? WHERE p_uuid=?", (server_info.new_uuid, server_info.old_uuid))
    cur.execute("UPDATE player_research SET p_uuid=? WHERE p_uuid=?", (server_info.new_uuid, server_info.old_uuid))
    con.commit()
    con.close()
