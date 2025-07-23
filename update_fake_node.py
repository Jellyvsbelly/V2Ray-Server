import json
import random

FILE_PATH = "grpc-server"

# مقداردهی الکی
days_left = random.randint(1, 7)
gb_left = random.randint(1, 20)

# کانفیگ ساختگی
fake_node = {
    "v": "2",
    "ps": f"⚠️ {days_left} روز و {gb_left} گیگ باقی مانده",
    "add": "fake.domain.com",
    "port": "443",
    "id": "00000000-0000-0000-0000-000000000000",
    "aid": "0",
    "net": "tcp",
    "type": "none",
    "host": "",
    "path": "/",
    "tls": "tls"
}

# خواندن لیست فعلی (base64 نیست؟)
with open(FILE_PATH, "r", encoding="utf-8") as f:
    try:
        config = json.load(f)
    except:
        config = []

# حذف کانفیگ قبلی جعلی
config = [node for node in config if not node["ps"].startswith("⚠️")]

# افزودن کانفیگ جدید
config.append(fake_node)

# ذخیره‌سازی
with open(FILE_PATH, "w", encoding="utf-8") as f:
    json.dump(config, f, ensure_ascii=False, indent=2)
