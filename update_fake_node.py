import random
from datetime import datetime

FILE_PATH = "grpc-server"

# ساخت متن کانفیگ جعلی
days_left = random.randint(1, 7)
gb_left = random.randint(1, 20)

fake_link = f"vless://00000000-0000-0000-0000-000000000000@fake.domain.com:443?type=grpc&encryption=none#⚠️ {days_left} روز و {gb_left} گیگ مونده"

# خواندن فایل اصلی
with open(FILE_PATH, "r", encoding="utf-8") as f:
    lines = f.readlines()

# حذف کانفیگ‌های فیک قبلی (اونی که با ⚠️ شروع می‌شن)
lines = [line for line in lines if not "⚠️" in line]

# اضافه کردن کانفیگ جدید به آخر فایل
lines.append(fake_link + "\n")

# ذخیره‌سازی
with open(FILE_PATH, "w", encoding="utf-8") as f:
    f.writelines(lines)

print(f"✅ کانفیگ فیکی با {days_left} روز و {gb_left} گیگ اضافه شد.")
