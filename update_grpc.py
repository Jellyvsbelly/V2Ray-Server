import json
import requests
from datetime import datetime

def get_fake_config():
    hour = datetime.utcnow().hour  # ساعت به وقت UTC
    total = 10737418240  # 10 گیگ
    used = int((hour / 24) * total)

    return {
        "v": "2",
        "ps": f"🔴 مصرف امروز: {int((used / total) * 100)}٪",
        "add": "fake.server.com",
        "port": "443",
        "id": "00000000-0000-0000-0000-000000000000",
        "aid": "0",
        "net": "grpc",
        "type": "none",
        "host": "fake.server.com",
        "path": "fake",
        "tls": "tls",
        "sni": "fake.server.com",
        "total": total,
        "up": used,
        "down": 0,
        "expiry": 1946086399
    }

def update_grpc_list():
    url = "https://raw.githubusercontent.com/Jellyvsbelly/V2Ray-Server/refs/heads/main/grpc-server"
    response = requests.get(url)
    data = response.text.strip()

    configs = [get_fake_config()]
    for line in data.splitlines():
        try:
            config = json.loads(line)
            if config.get("ps", "").startswith("🔴 مصرف امروز"):
                continue
            configs.append(config)
        except json.JSONDecodeError:
            continue

    with open("grpc-server", "w", encoding="utf-8") as f:
        for cfg in configs:
            f.write(json.dumps(cfg, ensure_ascii=False) + "\n")

if __name__ == "__main__":
    update_grpc_list()
