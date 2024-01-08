---
layout: page
title: common/airpaste (فارسی)
description: "اشتراک گذاری پیام و فایل از طریق شبکه مشترک با استفاده از mDNS."
content_hash: ad08f58806d96eacfee8511d4af57b5475a8caad
last_modified_at: 2024-01-08
related_topics:
  - title: English version
    url: /en/common/airpaste.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/airpaste.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/airpaste.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/airpaste.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/airpaste.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/airpaste.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/airpaste.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/airpaste.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/airpaste.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/airpaste.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># airpaste

اشتراک گذاری پیام و فایل از طریق شبکه مشترک با استفاده از mDNS.
اطلاعات بیشتر: <https://github.com/mafintosh/airpaste>.

- منتظر پیام می ماند و هنگام دریافت آن را نشان می دهد:

`airpaste`

- ارسال متن:

`echo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">text</span>` | airpaste`

- ارسال فایل:

`airpaste < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- دریافت فایل:

`airpaste > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- ساخت یا ورود به یک کانال:

`airpaste `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">channel_name</span>
