---
layout: page
title: common/catimg (فارسی)
description: "چاپ عکس در ترمینال."
content_hash: 27ffe1fd2d380de1e607b6a05ab2732dd2530d0a
last_modified_at: 2024-01-05
related_topics:
  - title: English version
    url: /en/common/catimg.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/catimg.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># catimg

چاپ عکس در ترمینال.
موارد مشابه: `pixterm`, `chafa`.
اطلاعات بیشتر: <https://github.com/posva/catimg>.

- چاپ یک JPEG, PNG, یا GIF در ترمینال:

`catimg `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- دوبرابر کردن وضوح یک تصویر:

`catimg -r 2 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- غیرفعال سازی رنگ 24 بیتی برای پشتیبانی بهتر ترمینال:

`catimg -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- مشخص کردن طول و عرض دلخواه:

`catimg `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-w|-H</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">40</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>
