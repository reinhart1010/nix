---
layout: page
title: common/bpkg (فارسی)
description: "یک پکیج منیجر برای بش اسکریپت."
content_hash: 7477895da1112317095e86f925e9ecffa6a2b7fc
last_modified_at: 2024-07-23
related_topics:
  - title: English version
    url: /en/common/bpkg.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/bpkg.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/bpkg.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># bpkg

یک پکیج منیجر برای بش اسکریپت.
اطلاعات بیشتر: <https://github.com/bpkg/bpkg>.

- بروزرسانی فهرست محلی:

`bpkg update`

- نصب یک بسته به صورت گلوبال:

`bpkg install --global `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- نصب یک بسته در یک زیرپوشه در پوشه ی کنونی:

`bpkg install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- نصب یک نسخه خاص از یک بسته به صورت گلوبال:

`bpkg install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">version</span>` -g`

- نمایش جزئیات یک بسته خاص:

`bpkg show `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- اجرای یک دستور، آرگومان ها به صورت اختیاری نوشته شده اند:

`bpkg run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">argument1 argument2 ...</span>
