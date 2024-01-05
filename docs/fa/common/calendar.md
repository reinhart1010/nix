---
layout: page
title: common/calendar (فارسی)
description: "نمایش رویداد های پیش رو با استفاده از یک فایل تقویم."
content_hash: acd235ff1fe6a3ecfaaa4c058627f2e5324d6022
last_modified_at: 2024-01-05
related_topics:
  - title: English version
    url: /en/common/calendar.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/calendar.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/calendar.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># calendar

نمایش رویداد های پیش رو با استفاده از یک فایل تقویم.
اطلاعات بیشتر: <https://www.commandlinux.com/man-page/man1/calendar.1.html>.

- نمایش رویداد های امروز و فردا (یا آخر هفته یعنی روز جمعه) با استفاده از تقویم پیشفرض:

`calendar`

- نگاهی به آینده، نمایش رویداد های 30 روز آینده:

`calendar -A `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">30</span>

- نگاهی به گذشته، نمایش رویداد های هفت روز گذشته:

`calendar -B `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">7</span>

- نمایش رویداد ها با استفاده از یک فایل تقویم دلخواه:

`calendar -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>
