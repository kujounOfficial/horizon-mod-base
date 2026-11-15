import json
import os
import zipfile
from pathlib import Path

NATIVE_FILE = "horizon-native.json"


def check_if_exists(path):
    return os.path.exists(path)


def get_mod_id():
    if not check_if_exists(NATIVE_FILE):
        return None

    with open(NATIVE_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)
        return data.get("id", None)


def check_mixin_toml():
    if not check_if_exists("mixins"):
        print("Mixins directory does not exist")
        return False

    mod_id = get_mod_id()
    if mod_id is None:
        print("Mod ID could not be found")
        return False

    if check_if_exists(f"mixins/{mod_id}/horizon-mixin.toml"):
        return True

    print("horizon-mixin.toml file does not exist")
    return False


def check_mod():
    if not check_if_exists(NATIVE_FILE):
        print(f"{NATIVE_FILE} file does not exist")
        return False

    return check_mixin_toml()


def walk_directory(mod_zip, current_path, root_path):
    for item in current_path.iterdir():
        arcname = item.relative_to(root_path.parent)

        if item.is_file():
            mod_zip.write(item, arcname=arcname)
            print(f"Added file: {arcname}")

        elif item.is_dir():
            mod_zip.write(item, arcname=arcname)
            print(f"Added directory: {arcname}")

            walk_directory(mod_zip, item, root_path)


def build_mod():
    mod_id = get_mod_id()

    with zipfile.ZipFile(f"{mod_id}.hmod", "w", zipfile.ZIP_DEFLATED) as mod_zip:
        mod_zip.write(NATIVE_FILE)

        mixin_path = Path(f"mixins/{mod_id}")
        mod_zip.write(mixin_path)

        walk_directory(mod_zip, mixin_path, root_path=Path("."))

        print("Mod build complete")


def main():
    if not check_mod():
        print("Mod is invalid")
        return False

    print("Mod is valid")
    build_mod()


main()