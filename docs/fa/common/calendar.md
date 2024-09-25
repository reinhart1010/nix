---
layout: page
title: common/calendar (فارسی)
description: "نمایش رویداد های پیش رو با استفاده از یک فایل تقویم."
content_hash: fa098846d2f8d31d180b50d75baee8f40d0c6177
last_modified_at: 2024-09-25
related_topics:
  - title: English version
    url: /en/common/calendar.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/calendar.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/calendar.html
    icon: bi bi-globe
tldri18n_status: 2
---
# calendar

نمایش رویداد های پیش رو با استفاده از یک فایل تقویم.
اطلاعات بیشتر: <https://manned.org/calendar>.

- نمایش رویداد های امروز و فردا (یا آخر هفته یعنی روز جمعه) با استفاده از تقویم پیشفرض:

`calendar`

- نگاهی به آینده، نمایش رویداد های 30 روز آینده:

`calendar -A `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">30</span>

- نگاهی به گذشته، نمایش رویداد های هفت روز گذشته:

`calendar -B `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">7</span>

- نمایش رویداد ها با استفاده از یک فایل تقویم دلخواه:

`calendar -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>
