---
layout: page
title: common/whereis (فارسی)
description: "پیداکردن فایل اجرایی، سورس، صفحه راهنما برای یک دستور."
content_hash: 9863d960137787399ba4ba32bf49a13ee1c33993
related_topics:
  - title: English version
    url: /en/common/whereis.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/whereis.html
    icon: bi bi-globe
---
# whereis

پیداکردن فایل اجرایی، سورس، صفحه راهنما برای یک دستور.
اطلاعات بیشتر: <https://manned.org/whereis>.

- پیداکردن فایل اجرایی، سورس و صفحه راهنما برای ssh:

`whereis `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ssh</span>

- پیداکردن فایل اجرایی و صفحه راهنما برای ls:

`whereis -bm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ls</span>

- پیداکردن سورس برای gcc و صفحه راهنما برای git:

`whereis -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gcc</span>` -m `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">git</span>

- پیداکردن فایل اجرایی برای gcc در مسیر `/usr/bin/`:

`whereis -b -B `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/usr/bin/</span>` -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gcc</span>

- پیدا کردن فایل های اجرایی غیر عادی(برای آنهایی که بیشتر از یک فایل اجرایی در سیستم دارند):

`whereis -u *`

- پیدا کردن صفحات راهنمای غیر عادی(برای آنهایی که بیشتر از یک فایل اجرایی در سیستم دارند):

`whereis -u -m *`
