---
layout: page
title: common/7zr (فارسی)
description: "بایگانی کننده فایل با فشرده سازی بالا."
content_hash: 37d4c97f8a060bf0c86351602f714c8caa140f93
last_modified_at: 2023-11-12
related_topics:
  - title: বাংলা version
    url: /bn/common/7zr.html
    icon: bi bi-globe
  - title: Deutsch version
    url: /de/common/7zr.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/7zr.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/7zr.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/7zr.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/7zr.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/7zr.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/7zr.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/7zr.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/7zr.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/7zr.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/7zr.html
    icon: bi bi-globe
  - title: português (Portugal) version
    url: /pt_PT/common/7zr.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/7zr.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/7zr.html
    icon: bi bi-globe
tldri18n_status: 2
---
# 7zr

بایگانی کننده فایل با فشرده سازی بالا.
مشابه `7z` منحصر به پشتیبانی از فایل های `.7z`.
اطلاعات بیشتر: <https://manned.org/7zr>.

- بایگانی کردن یک فایل یا پوشه :

`7zr a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">مسیر/به/بایگانی.7z</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">مسیر/به/فایل_یا_پوشه</span>

- رمزگذاری یک بایگانی (همراه با نام فایل ها) موجود :

`7zr a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">مسیر/به/فایل_رمزگذاری_شده.7z</span>` -p`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">گذرواژه</span>` -mhe=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">on</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">مسیر/به/بایگانی.7z</span>

- استخراج یک بایگانی با نگهداری ساختار پوشه اصلی :

`7zr x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">مسیر/به/بایگانی.7z</span>

- استخراج یک بایگانی به پوشه معین :

`7zr x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">مسیر/به/بایگانی.7z</span>` -o`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">مسیر/به/خروجی</span>

- استخراج یک بایگانی به خروجی استاندارد `stdout` :

`7zr x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">مسیر/به/بایگانی.7z</span>` -so`

- فهرست نمودن محتویات یک بایگانی :

`7zr l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">مسیر/به/بایگانی.7z</span>

- فهرست نمودن انواع بایگانی های موجود :

`7zr i`
