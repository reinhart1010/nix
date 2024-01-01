---
layout: page
title: common/export (فارسی)
description: "دستور تغییر متغییرهای محلی سیستم موجود برای پروسه های جدید."
content_hash: 97e6e74ce2c1a31d5605c4d55eed85253bc5fd27
last_modified_at: 2024-01-01
related_topics:
  - title: Deutsch version
    url: /de/common/export.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/export.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/export.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># export

دستور تغییر متغییرهای محلی سیستم موجود برای پروسه های جدید.
اطلاعات بیشتر: <https://pubs.opengroup.org/onlinepubs/9699919799/utilities/V3_chap02.html#export>.

- ایجاد و تعیین مقدار یک متغییر جدید:

`export `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">متغییر</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">مقدار</span>

- حذف یک متغییر سیستمی:

`export -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">متغییر</span>

- افزودن یک تابع شل به متغییر سیستمی:

`export -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">نام تابع</span>

- افزودن یک مسیر به متغییر $PATH:

`export PATH=$PATH:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">مسیر/برای/افزودن</span>
