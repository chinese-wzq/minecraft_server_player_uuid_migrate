import action.base as base
import os
import sqlite3


def process(server_info: base.ServerInfo):
    db_path = os.path.join(server_info.server_path, 'plugins', 'LWC', 'lwc.db')
    base.backup_file(db_path, "LWC", server_info, True)
    con = sqlite3.connect(db_path)
    cur = con.cursor()
    cur.execute("UPDATE lwc_protections SET owner = ? WHERE owner = ?;", (server_info.new_uuid, server_info.old_uuid))
    con.commit()
    con.close()
