---
layout: page
title: linux/caja (فارسی)
description: "مدیریت فایلها و پوشه ها در محیط دسکتاپ MATE."
content_hash: da98b40fd150e4c2a047a301520e3394f2277a9a
last_modified_at: 2024-04-11
related_topics:
  - title: English version
    url: /en/linux/caja.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/caja.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># caja

مدیریت فایلها و پوشه ها در محیط دسکتاپ MATE.
اطلاعات بیشتر: <https://manned.org/caja>.

- باز کردن پوشه خانگی کاربر کنونی:

`caja`

- بازکردن پوشه های مشخص شده در پنجره جداگانه:

`caja `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory1 path/to/directory2 ...</span>

- بازکردن پوشه های مشخص شده در تب ها:

`caja --tabs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory1 path/to/directory2 ...</span>

- بازکدن یک پوشه در یک پنجره با اندازه مشخص:

`caja --geometry=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">600</span>`x`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">400</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- بستن همه پنجره ها:

`caja --quit`
