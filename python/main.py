import argparse
import json
import re
from pathlib import Path
import subprocess
import os

base_dir = Path(__file__).resolve().parent.parent
rules_file = base_dir / "extension" / "rules.json"
filter_file = base_dir / "python" / "filters.txt"

block_types = [
    "script",
    "image",
    "xmlhttprequest",
    "sub_frame",
    "stylesheet",
    "media",
    "font"
]
def banner():
    os.system("cls" if os.name == "nt" else "clear")

    print(PURPLE + r"""
 _   _ __  __ _____  __   __
| | | |  \/  | ____| \ \ / /
| |_| | |\/| |  _|    \ V /
|  _  | |  | | |___   / / \
|_| |_|_|  |_|_____| /_/ \_\

""" + RESET)

    print(CYAN + "           HM3X ADBLOCK" + RESET)
    print(WHITE + "       ----------------------" + RESET)
    print(PURPLE + "       Version : 0.1.0" + RESET)
    print(CYAN + "       Developer : Hm3x" + RESET)
    print(RESET)


def open_chrome_extensions():
    chrome_paths = [
        os.path.expandvars(
            r"%ProgramFiles%\Google\Chrome\Application\chrome.exe"
        ),
        os.path.expandvars(
            r"%ProgramFiles(x86)%\Google\Chrome\Application\chrome.exe"
        ),
        os.path.expandvars(
            r"%LOCALAPPDATA%\Google\Chrome\Application\chrome.exe"
        )
    ]
    for path in chrome_paths:
        if os.path.exists(path):
            subprocess.Popen([
                path,
                "chrome://extensions/"
            ])
            print("**** Chrome eklentiler sayfası açıldı!")
            return

    print("**** Chrome bulunamadı!")
def load_filters():
    if not filter_file.exists():
        return set()


    return {
        line.strip().lower()
        for line in filter_file.read_text(encoding="utf-8").splitlines()
        if line.strip()
    }

def save_filters(filters):
    filter_file.parent.mkdir(parents=True,exist_ok=True)

    filter_file.write_text(
        "\n".join(sorted(filters)),
        encoding="utf-8"
    )

def generate_rules(filters):
    rules = []

    for rule_id,domain in enumerate(sorted(filters),start=1):
        rules.append({
            "id":rule_id,
            "priority":1,
            "action":{
                "type":"block"
            },
            "condition":{
                "urlFilter":f"||{domain}^",
                "resourceTypes":block_types
            }
        })

    rules_file.write_text(
        json.dumps(rules,indent=4,ensure_ascii=False),
        encoding="utf-8"
    )
    open_chrome_extensions()
def valid_domain(domain):
    return bool(
        re.fullmatch(
            r"(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}",
            domain
        )
    )
def main():
    parser = argparse.ArgumentParser(
        description="HmexAdsBlock Reklam engelleme aracı"
    )
    subparsers = parser.add_subparsers(dest="command",required=True)

    block_parser = subparsers.add_parser("block")
    block_parser.add_argument("domain")

    unblock_parser = subparsers.add_parser("unblock")
    unblock_parser.add_argument("domain")

    subparsers.add_parser("list")

    args = parser.parse_args()
    filters = load_filters()

    if args.command == "block":
        domain = args.domain.lower().strip()

        if not valid_domain(domain):
            print("**** Geçersiz Alan adı!")
            return
        if domain in filters:
            print("**** Bu Alan adı zaten engelleniyor.")
            return
    
        filters.add(domain)
        save_filters(filters)
        generate_rules(filters)

        print(f"**** Engelleme Eklendi: {domain}")
        print("**** Chrome'a eklentiyi yeniden yükle.")
       
        
    elif args.command == "unblock":
        domain = args.domain.lower().strip()


        if domain not in filters:
            print("**** Bu Alan adı listede bulunamadı.")
            return

        filters.remove(domain)
        save_filters(filters)
        generate_rules(filters)

        print(f"**** Engelleme kaldırıldı: {domain}")
        print("**** Chrome'a eklentiyi yeniden yükle.")
       
    elif args.command == "list":
        if not filters:
            print("**** Henüz özel engelleme kuralın yok.")
        else:
            for domain in sorted(filters):
                print(domain)


if __name__ == "__main__":
    main()