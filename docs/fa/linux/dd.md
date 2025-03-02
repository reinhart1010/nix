---
layout: page
title: linux/dd (فارسی)
description: "تبدیل و کپی یک فایل."
content_hash: fbe878f20a02cb3638dc852dd7f4addc7e3ace32
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/linux/dd.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/dd.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/dd.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/dd.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/dd.html
    icon: bi bi-globe
tldri18n_status: 2
---
# dd

تبدیل و کپی یک فایل.
اطلاعات بیشتر: <https://www.gnu.org/software/coreutils/manual/html_node/dd-invocation.html>.

- ساخت یک درایو USB قابل بوت از یک فایل iso (مثل `archlinux-xxx.iso`) و نمایش پیشرفت:

`dd if=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.iso</span>` of=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/usb_drive</span>` status=progress`

- کلون کردن یک درایو به یک درایو دیگر با اندازهٔ بلوک ۴ مگابایت و اعمال چیزهای نوشته شده پیش از خاتمهٔ دستور:

`dd bs=4M conv=fsync if=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/source_drive</span>` of=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/dest_drive</span>

- ایجاد یک فایل با تعداد مشخصی بایت تصادفی با استفاده از درایور random کرنل:

`dd bs=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">100</span>` count=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1</span>` if=/dev/urandom of=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/random_file</span>

- ارزیابی عملکرد نوشتن روی یک دیسک:

`dd bs=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1M</span>` count=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1024</span>` if=/dev/zero of=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file_1GB</span>

- ساخت یک پشتیبان از سامانه و ذخیرهٔ آن در یک فایل IMG (می‌توان بعداً با تغییر `if` به `of` آن را بازسازی کرد):

`dd if=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/drive_device</span>` of=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.img</span>` status=progress`

- بررسی پیشرفت یک عملکرد در حال اجرای `dd` (این دستور را از یک پوستهٔ دیگر اجرا کنید):

`kill -USR1 $(pgrep -x dd)`
