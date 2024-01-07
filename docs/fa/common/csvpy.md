---
layout: page
title: common/csvpy (فارسی)
description: "اجرای یک فایل CSV در شل پایتون."
content_hash: dbfcc4ad1c74930e89d285d42fc86c9be2f5d74b
last_modified_at: 2024-01-07
related_topics:
  - title: English version
    url: /en/common/csvpy.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/csvpy.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/csvpy.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/csvpy.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># csvpy

اجرای یک فایل CSV در شل پایتون.
در csvkit گنجانده شده است.
اطلاعات بیشتر: <https://csvkit.readthedocs.io/en/latest/scripts/csvpy.html>.

- بارگذاری یک فایل CSV در یک آبجت از نوع `CSVKitReader`:

`csvpy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">data.csv</span>

- اجرای یک فایل CSV در یک آبجکت `CSVKitDictReader`:

`csvpy --dict `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">data.csv</span>
