import action
import gettext


def migrate(server_info: action.ServerInfo):
    action.migrate_saves(server_info)
    action.migrate_usercache(server_info)
    action.plugin_migrate(server_info)


def main():
    print(_("这是一个工具，用于将一个UUID上的所有可迁移的数据覆盖迁移到另一个UUID上"))
    print(_("对于MCDR服务器，你的服务器路径应该为服务端的路径，而不是MCDR的路径"))
    print(_("注意，仅适用于bukkit系服务器（包括spigot、paper等）"))
    server_path = input(_("请输入服务器的路径："))
    old_uuid = input(_("请输入旧的UUID："))
    new_uuid = input(_("请输入新的UUID："))
    server_info = action.ServerInfo(server_path, old_uuid, new_uuid)
    migrate(server_info)


choose = input("语言/Language: 1.简体中文 2.English")
if choose == "1":
    gettext.install("zh_cn", "locale")
else:
    gettext.install("en_us", "locale")
main()
