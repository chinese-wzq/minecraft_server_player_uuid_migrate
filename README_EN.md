# Minecraft Server Player UUID Migration Tool
[中文](README.md) | [English](README_EN.md)

This is a simple tool for migrating all migratable data on one UUID to another UUID. It is suitable for Bukkit-based servers, including but not limited to Spigot, Paper, etc., but does not support vanilla servers or Fabric-based servers. In fact, if the world save is divided into three folders named world, world_nether, world_the_end, and the plugins folder is plugins, you can also give it a try.

## Features
- Supports the migration of player data and plugin data.
- Easy-to-use command-line interface.
- The data migration of the plugin is scalable; you can freely add unsupported programs for migrating plugin data. (Simply refer to other files under the action/plugins_process/ directory to write your own.)

## Installation

Before you begin, make sure you have the Python environment installed.

## Usage Instructions

1. Clone the repository to your local machine.
```bash
git clone https://github.com/your-username/uuid-migrate-tool.git
cd uuid-migrate-tool
```

2. Run the migration tool.
```bash
python main.py
```

3. Follow the prompts to enter the server path, old UUID, and new UUID.

## Contribution

If you have any suggestions or want to contribute code (such as more plugin support), please submit a Pull Request or create an Issue.

## License

This project is licensed under [GPL-3.0](LICENSE).