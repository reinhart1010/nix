---
layout: page
title: common/echo (فارسی)
description: "چاپ ورودی داده شده."
content_hash: 6c6a049f5a69498d78cbc91ca6f7f915430908d6
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/echo.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/echo.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/echo.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/echo.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/echo.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/echo.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/echo.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/echo.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/echo.html
    icon: bi bi-globe
  - title: српски version
    url: /sr/common/echo.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/echo.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/common/echo.html
    icon: bi bi-globe
tldri18n_status: 2
---
# echo

چاپ ورودی داده شده.
اطلاعات بیشتر: <https://www.gnu.org/software/coreutils/echo>.

- چاپ پیام ورودی. نکته : استفاده از علامت نقل قول انتخابی است:

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">سلام دنیا</span>`"`

- چاپ یک پیام حاوی متغییرهای سیستمی:

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">مسیر سیستم من $PATH است.</span>`"`

- چاپ یک پیام بدون انتقال به خط جدید:

`echo -n "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">سلام دنیا</span>`"`

- افزودن یک پیام به انتهای یک فایل:

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">سلام دنیا</span>`" >> `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">فایل.متنی</span>

- فعال کردن تفسیر کاراکترهای خاص، برای مثال tab:

`echo -e "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ستون 1\tستون 2</span>`"`

- چاپ وضعیت خروج آخرین دستور اجرا شده (نکته: معادل های این دستور در ویندور به ترتیب echo %errorlevel% و $lastexitcode هستند.) :

`echo $?`
