#!/usr/bin/env python3
"""Generates pluginmaster.json from individual plugin manifests in plugins/."""
import json
from pathlib import Path

PLUGINS_DIR = Path(__file__).parent / "plugins"
OUTPUT = Path(__file__).parent / "pluginmaster.json"

def main():
    plugins = []
    for manifest_path in sorted(PLUGINS_DIR.glob("*/manifest.json")):
        with open(manifest_path, "r", encoding="utf-8") as f:
            manifest = json.load(f)
        plugins.append(manifest)
        print(f"  Added: {manifest.get('InternalName', '?')} v{manifest.get('AssemblyVersion', '?')}")
    with open(OUTPUT, "w", encoding="utf-8") as f:
        json.dump(plugins, f, indent=2, ensure_ascii=False)
    print(f"Generated pluginmaster.json with {len(plugins)} plugin(s)")

if __name__ == "__main__":
    main()
