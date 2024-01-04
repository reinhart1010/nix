---
layout: page
title: linux/abbr (فارسی)
description: "fish shell مدیریت مخفف های"
content_hash: 5a0fa576a58c8f114ed169f868d653f4cfa70978
last_modified_at: 2024-01-04
related_topics:
  - title: català version
    url: /ca/linux/abbr.html
    icon: bi bi-globe
  - title: Deutsch version
    url: /de/linux/abbr.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/abbr.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/abbr.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/abbr.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/linux/abbr.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/abbr.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/abbr.html
    icon: bi bi-globe
tldri18n_status: 2
---
# abbr

fish shell مدیریت مخفف های
جایگزین کردن کلمات وارد شده توسط کاربر با جملات طولانی
اطلاعات بیشتر: <https://fishshell.com/docs/current/cmds/abbr.html>.

- اضافه کردن مخفف جدید:

`abbr --add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">نام_اختصاری</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">دستور</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">آرگومان_های_دستور</span>

- تغییر نام یک مخفف موجود:

`abbr --rename `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">نام_قدیمی</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">نام_جدید</span>

- پاک کردن یک مخفف موجود:

`abbr --erase `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">نام_مخفف</span>

- وارد کردن یک مخفف وارد شده در یک میزبان دیگر از طریق ssh:

`ssh `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">نام_میزبان</span>` abbr --show | source`
