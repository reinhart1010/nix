---
layout: page
title: common/df (فارسی)
description: "یک نمای کلی از میزان استفاده فضای دیسک و سیستم فایل ارائه می‌دهد."
content_hash: 4c5fce215a50d2d29d36f4a9740761f73b47d322
last_modified_at: 2024-01-05
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
tldri18n_status: 2
---
# df

یک نمای کلی از میزان استفاده فضای دیسک و سیستم فایل ارائه می‌دهد.
اطلاعات بیشتر: <https://www.gnu.org/software/coreutils/df>.

- نمایش تمامی سیستم‌های فایل و فضای دیسک آن‌ها :

`df`

- نمایش تمامی سیستم‌های فایل و استفاده از حالت خوانا برای فضای دیسک آن‌ها :

`df -h`

- نمایش سیستم‌فایل و فضای دیسک آن شامل فایل یا دایرکتوری داده شده :

`df `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file_or_directory</span>

- نمایش آمار تعداد درایوهای آزاد :

`df -i`

- نمایش سیستم‌های فایل با حذف انواع مشخص شده :

`df -x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">squashfs</span>` -x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tmpfs</span>
