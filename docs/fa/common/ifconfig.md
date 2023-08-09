---
layout: page
title: common/ifconfig (فارسی)
description: "تنظیم کننده رابط های شبکه."
content_hash: 78f67846dcdda0c52495675837ae2a600b6909c5
last_modified_at: 2023-08-09
related_topics:
  - title: English version
    url: /en/common/ifconfig.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/ifconfig.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># ifconfig

تنظیم کننده رابط های شبکه.
اطلاعات بیشتر: <https://net-tools.sourceforge.io/man/ifconfig.8.html>.

- نمایش تنظیمات شبکه یک کارت شبکه :

`ifconfig eth0`

- نمایش جزئیات تمامی رابط ها، مشمول رابط های غیرفعال میشود :

`ifconfig -a`

- غیرفعال کردن رابط eth0 :

`ifconfig eth0 down`

- فعال کردن رابط eth0 :

`ifconfig eth0 up`

- اختصاص آدرس ای پی به رابط eth0 :

`ifconfig eth0 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">آدرس_ای_پی</span>
