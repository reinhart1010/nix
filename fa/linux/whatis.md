---
layout: page
title: linux/whatis (فارسی)
description: "نمایش توضیحات یک خطی از صفحات راهنما."
content_hash: dfa03e73d47742d586dedc1cca7732ca6b0213c2
related_topics:
  - title: English version
    url: /en/linux/whatis.html
    icon: bi bi-globe
---
# whatis

نمایش توضیحات یک خطی از صفحات راهنما.

- نمایش توضیحات یک دستور از صفحات راهنما:

`whatis `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>

- توضیحات در آخر خط ترمینال برش نمی خورد:

`whatis --long `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>

- نمایش توضیحات تمامی دستورات مطابق با الگو:

`whatis --wildcard `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">net*</span>

- جستجو در توضیحات صفحات راهنما با عبارات منظم:

`whatis --regex '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">wish[0-9]\.[0-9]</span>`'`
