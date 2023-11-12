---
layout: page
title: linux/whatis (فارسی)
description: "نمایش توضیحات یک خطی از صفحات راهنما."
content_hash: 5bf1009a1d02cd82c06ea46863d3cd7eeb959f5e
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/linux/whatis.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/linux/whatis.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># whatis

نمایش توضیحات یک خطی از صفحات راهنما.
اطلاعات بیشتر: <https://manned.org/whatis>.

- نمایش توضیحات یک دستور از صفحات راهنما:

`whatis `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>

- توضیحات در آخر خط ترمینال برش نمی خورد:

`whatis --long `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>

- نمایش توضیحات تمامی دستورات مطابق با الگو:

`whatis --wildcard `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">net*</span>

- جستجو در توضیحات صفحات راهنما با عبارات منظم:

`whatis --regex '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">wish[0-9]\.[0-9]</span>`'`
