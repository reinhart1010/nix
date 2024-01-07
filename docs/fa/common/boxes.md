---
layout: page
title: common/boxes (فارسی)
description: "کشیدن، حذف و تعمیر جعبه های هنری اسکی."
content_hash: 6ad1447eeebd1c1c220cea2bd9e34086a01b56b2
last_modified_at: 2024-01-07
related_topics:
  - title: English version
    url: /en/common/boxes.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/boxes.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/boxes.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># boxes

کشیدن، حذف و تعمیر جعبه های هنری اسکی.
اطلاعات بیشتر: <https://boxes.thomasjensen.com>.

- کشیدن یک جعبه در اطراف یک رشته:

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">string</span>`" | boxes`

- حذف جعبه از یک رشته:

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">string</span>`" | boxes -r`

- کشیدن یک جعبه با طرح دلخواه در اطراف یک رشته:

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">string</span>`" | boxes -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">parchment</span>

- کشیدن یک جعبه به طول 10 و ارتفاع 5:

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">string</span>`" | boxes -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>`x`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5</span>

- کشیدن یک جعبه با متن در وسط:

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">string</span>`" | boxes -a c`
