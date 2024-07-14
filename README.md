# 我的世界服务器玩家UUID迁移工具
[中文](README.md) | [English](README_EN.md)

这是一个简单的工具，用于将一个UUID上的所有可迁移的数据覆盖迁移到另一个UUID上。它适用于bukkit系服务器，包括但不限于spigot、paper等，但不支持原版服务器或fabric系服务器。实际上，如果保存世界是分为三个文件夹world、world_nether、world_the_end，插件文件夹为plugins，那么你也可以试试看。

## 特点
- 支持迁移玩家数据、插件数据。
- 易于使用的命令行界面。
- 插件的数据迁移可扩展，你可以自由增加用于迁移插件数据的没有被支持的程序。（只需要参考其它action/plugins_process/下的文件即可自己编写）

## 安装

在开始之前，请确保您已经安装了Python环境。

## 使用说明

1. 克隆仓库到本地机器。
```bash
git clone https://github.com/your-username/uuid-migrate-tool.git
cd uuid-migrate-tool
```

2. 运行迁移工具。
```bash
python migrate.py
```

3. 按照提示输入服务器路径、旧UUID和新UUID。

## 贡献

如果您有任何建议或想要贡献代码（比如更多的插件支持），请提交Pull Request或创建Issue。

## 许可

本项目采用[GPL-3.0](LICENSE)。
