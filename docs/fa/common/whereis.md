---
layout: page
title: common/whereis (فارسی)
description: "پیداکردن فایل اجرایی، سورس، صفحه راهنما برای یک دستور."
content_hash: a9807a79c2113f5cbd8ee72fdd66b88c13694e98
last_modified_at: 2024-03-14
related_topics:
  - title: English version
    url: /en/common/whereis.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/whereis.html
    icon: bi bi-globe
tldri18n_status: 2
---
# whereis

پیداکردن فایل اجرایی، سورس، صفحه راهنما برای یک دستور.
اطلاعات بیشتر: <https://manned.org/whereis>.

- پیداکردن فایل اجرایی، سورس و صفحه راهنما برای SSH:

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
