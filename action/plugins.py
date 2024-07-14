import action.base as base
import traceback
import os


def plugin_migrate(server_info: base.ServerInfo):
    server_path = server_info.server_path
    plugins = [i for i in os.listdir(server_path + "/plugins") if
               os.path.isdir(os.path.join(server_path + "/plugins", i))]
    print(_("等待迁移的插件配置文件夹：%s") % plugins)
    for plugin in plugins:
        plugin_process_programme_path = os.path.join("action", "plugins_process", f"{plugin}.py")
        if os.path.exists(plugin_process_programme_path):
            if input(_("处理插件%s吗？（y/n）") % plugin) != "y":
                continue
            print(_("正在处理插件%s...") % plugin)
            plugin_process_programme = __import__("action.plugins_process." + plugin, fromlist=[plugin])
            try:
                plugin_process_programme.process(server_info)
                print(_("插件%s处理完毕，没有遇到错误") % plugin)
            except Exception:
                print(_("哎呀X_X，处理%s时遇到了以下错误：") % plugin)
                traceback.print_exc()
        else:
            print(_("未找到插件%s的处理程序，跳过") % plugin)
