---
layout: page
title: common/boxes (فارسی)
description: "کشیدن، حذف و تعمیر جعبه های هنری اسکی."
content_hash: 458ea0b0b563524ca22cada0c5f725148e3944e3
last_modified_at: 2024-01-21
related_topics:
  - title: English version
    url: /en/common/boxes.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/boxes.html
    icon: bi bi-globe
tldri18n_status: 2
---
# boxes

کشیدن، حذف و تعمیر جعبه های هنری اسکی.
اطلاعات بیشتر: <https://boxes.thomasjensen.com/boxes-man-1.html>.

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
