from .. import base
import os
import sqlite3


def process(server_info: base.ServerInfo):
    db_path=os.path.join(server_info.server_path, 'plugins', 'LWC', 'lwc.db')
    con = sqlite3.connect(db_path)
    cur = con.cursor()
    update_query = f"""
        UPDATE lwc_protections
        SET owner = '{server_info.new_uuid}'
        WHERE owner = '{server_info.old_uuid}';
    """
    cur.execute(update_query)
    con.commit()
    con.close()