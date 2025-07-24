import random

file_path = "grpc-server"

# تعریف محدودیت کل
total_days = 7
total_gb = 30

# مقدارهای تصادفی باقی‌مانده
days_left = random.randint(1, total_days)
gb_left = random.randint(3, total_gb)

# محاسبه درصد مصرف‌شده
days_used_percent = round((1 - days_left / total_days) * 100)
gb_used_percent = round((1 - gb_left / total_gb) * 100)

# انتخاب ایموجی وضعیت و پرچم
flags = ["🇫🇷", "🇬🇧", "🇩🇪", "🇮🇷", "🇯🇵", "🇺🇸", "🇹🇷"]
flag = random.choice(flags)

# تعیین وضعیت کلی
if days_left <= 2 or gb_left <= 5:
    status = "⚠️ نزدیک اتمام!"
    emoji = "💀🔥"
elif days_left >= 5 and gb_left >= 15:
    status = "✅ وضعیت عالی"
    emoji = "💚✨"
else:
    status = "🟡 مصرف متوسط"
    emoji = "🌀🧭"

# متن نهایی با درصد
fake_tag = (
    f"{emoji} {days_left} روز و {gb_left} گیگ باقی‌مانده | {status} {flag} "
    f"| 📊 {gb_used_percent}% حجم مصرف‌شده | 📆 {days_used_percent}% زمان گذشته"
)

# لینک فیک نهایی
fake_link = (
    f"vless://00000000-0000-0000-0000-000000000000@fake.fake:443?"
    f"type=grpc&encryption=none#{fake_tag}"
)

# خواندن فایل موجود
try:
    with open(file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()
except FileNotFoundError:
    lines = []

# حذف کانفیگ فیک قبلی
lines = [line for line in lines if "00000000-0000-0000-0000-000000000000" not in line]

# اضافه به ابتدای فایل
lines.insert(0, fake_link + "\n")

# ذخیره فایل نهایی
with open(file_path, "w", encoding="utf-8") as f:
    f.writelines(lines)

print(f"✅ کانفیگ فیکی همراه با درصد اضافه شد:\n{fake_tag}")
