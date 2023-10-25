---
layout: page
title: linux/adduser (فارسی)
description: "ابزار اضافه‌ کردن کاربر."
content_hash: 64d383a5d971bb2520dc96ae252c2e5404b859e7
last_modified_at: 2023-10-25
related_topics:
  - title: Deutsch version
    url: /de/linux/adduser.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/adduser.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/adduser.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/linux/adduser.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/adduser.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/adduser.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># adduser

ابزار اضافه‌ کردن کاربر.
اطلاعات بیشتر: <https://manpages.debian.org/latest/adduser/adduser.html>.

- ایجاد یک کاربر جدید با دایرکتوری خانگی پیش‌فرض و درخواست از کاربر برای تنظیم رمز عبور:

`adduser `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">نام‌ کاربری</span>

- ایجاد یک کاربر جدید بدون دایرکتوری خانگی:

`adduser --no-create-home `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">نام‌ کاربری</span>

- ایجاد یک کاربر جدید با دایرکتوری خانگی در مسیر مشخص:

`adduser --home `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">مسیر/به/خانه</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">نام‌ کاربری</span>

- ایجاد یک کاربر جدید با تنظیم پوسته (shell) مشخص به عنوان پوسته ورود:

`adduser --shell `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">مسیر/به/پوسته</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">نام‌ کاربری</span>

- ایجاد یک کاربر جدید که به گروه مشخصی تعلق دارد:

`adduser --ingroup `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">گروه</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">نام‌ کاربری</span>
