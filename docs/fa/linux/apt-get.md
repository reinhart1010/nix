---
layout: page
title: linux/apt-get (فارسی)
description: "ابزار مدیریت بسته‌های دبیان و اوبونتو."
content_hash: a092fda3c6a7e13ed6fbe078c91be9a67ff20027
last_modified_at: 2024-01-05
related_topics:
  - title: العربية version
    url: /ar/linux/apt-get.html
    icon: bi bi-globe
  - title: català version
    url: /ca/linux/apt-get.html
    icon: bi bi-globe
  - title: Deutsch version
    url: /de/linux/apt-get.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/apt-get.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/apt-get.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/apt-get.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/linux/apt-get.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/apt-get.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/linux/apt-get.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/apt-get.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/linux/apt-get.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/linux/apt-get.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/apt-get.html
    icon: bi bi-globe
tldri18n_status: 2
---
# apt-get

ابزار مدیریت بسته‌های دبیان و اوبونتو.
جستجو در بسته‌ها با استفاده از `apt-cache`.
اطلاعات بیشتر: <https://manpages.debian.org/latest/apt/apt-get.8.html>.

- به‌روز‌رسانی لیست بسته‌ها و نسخه‌های موجود (توصیه می‌شود که این دستور را قبل از دیگر دستورات `apt-get` اجرا کنید):

`apt-get update`

- نصب یک بسته یا به روزرسانی آن به آخرین نسخه موجود:

`apt-get install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- حذف یک بسته:

`apt-get remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- حذف یک بسته و فایل‌های پیکربندی آن:

`apt-get purge `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- ارتقاء تمامی بسته‌های نصب شده به آخرین نسخه‌های موجود:

`apt-get upgrade`

- پاکسازی مخزن محلی - حذف فایل‌های بسته (`.deb`) از دانلودهای متوقف شده که دیگر قابل دانلود نیستند:

`apt-get autoclean`

- حذف تمام بسته‌هایی که دیگر نیازی به آن‌ها نیست:

`apt-get autoremove`

- ارتقاء بسته‌های نصب شده (مانند `upgrade`) اما با حذف بسته‌های قدیمی و نصب بسته‌های اضافی برای برآورده کردن وابستگی‌های جدید:

`apt-get dist-upgrade`
