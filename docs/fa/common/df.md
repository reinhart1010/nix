---
layout: page
title: common/df (فارسی)
description: "یک نمای کلی از میزان استفاده فضای دیسک و سیستم فایل ارائه می‌دهد."
content_hash: 464093ec5e24811bd3025b903e9ae304f931185b
last_modified_at: 2023-08-09
related_topics:
  - title: Deutsch version
    url: /de/common/df.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/df.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/df.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/df.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/df.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/df.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/df.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/df.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/common/df.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># df

یک نمای کلی از میزان استفاده فضای دیسک و سیستم فایل ارائه می‌دهد.
اطلاعات بیشتر: <https://www.gnu.org/software/coreutils/df>.

- نمایش تمامی سیستم‌های فایل و فضای دیسک آن‌ها :

`df`

- نمایش تمامی سیستم‌های فایل و استفاده از حالت خوانا برای فضای دیسک آن‌ها :

`df -h`

- نمایش سیستم‌فایل و فضای دیسک آن شامل فایل یا دایرکتوری داده شده :

`df `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">مسیر/به/فایل_یا_پوشه</span>

- نمایش آمار تعداد درایوهای آزاد :

`df -i`

- نمایش سیستم‌های فایل با حذف انواع مشخص شده :

`df -x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">squashfs</span>` -x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tmpfs</span>
