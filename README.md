# Horizon Mod Base

A starter template for creating mods for **Horizon Rust**. It comes with a ready-to-use project structure and a custom build script, `build.py`, that packages your source files into a working mod.

> This project is not an official product and is not affiliated with or endorsed by the Horizon developers.

## Features

- Ready-made mod skeleton to start from right away
- One command, `python build.py`, builds the mod into a usable package
- Included example mod demonstrating the basics:
  - **Enables flying** for the player
  - **Sends a chat message** whenever you interact (use) with a block

## Requirements

- [Python](https://www.python.org/downloads/) 3 or newer

No external Python packages are required. `build.py` uses only the standard library (`json`, `os`, `zipfile`, `pathlib`).

## Quick Start

```bash
git clone https://github.com/kujounOfficial/horizon-mod-base.git
cd horizon-mod-base
python build.py
```

When the build finishes, the packaged mod is created by the script.

## Building the Mod

The whole build is handled by `build.py`:

```bash
python build.py
```

The script reads the mod's configuration, collects the project files and packs them into a mod archive that Horizon can load.

## Installing the Mod

1. Run `python build.py`.
2. Copy the generated .hmod file into Horizon Rust's mods folder.
3. Launch Horizon Rust and enable the mod.

## The Example Mod

The base ships with a small example mod so you can see how everything fits together and verify that your setup works:

- **Flight:** when the mod loads, flying is enabled for the player.
- **Block interaction message:** every time you use (right-click) a block, a message is shown in the chat.

Use it as a reference, or remove it and replace it with your own logic.

## Creating Your Own Mod

1. Fork or clone this repository.
2. Rename the mod and update its metadata.
3. Modify or replace the example code (flight and block-use message) with your own.
4. Build with `python build.py` and test the result in Horizon.

## Credits

This project drew inspiration from [crosshair-indicator](https://github.com/CayMac97/crosshair-indicator) by [CayMac97](https://github.com/CayMac97). The original code has been heavily modified and reworked; only a small part of a single file remains similar. Thanks to the original author for the inspiration.

## License

See the `LICENSE` file for details. Any portion of code derived from crosshair-indicator remains subject to that project's license.

## Contributing

Issues and pull requests are welcome.
