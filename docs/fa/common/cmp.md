---
layout: page
title: common/cmp (فارسی)
description: "مقایسه بایت به بایت دو فایل."
content_hash: d27a16fa6cc9c00388366724a367496c34f6b1b5
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/cmp.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/cmp.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/cmp.html
    icon: bi bi-globe
tldri18n_status: 2
---
# cmp

مقایسه بایت به بایت دو فایل.
اطلاعات بیشتر: <https://www.gnu.org/software/diffutils/manual/html_node/Invoking-cmp.html>.

- نمایش کارکتر و خطی که اولین تفاوت دو فایل در آن یافت شد:

`cmp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">مسیر/به/فایل_اول</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">مسیر/به/فایل_دوم</span>

- نمایش اطلاعات اولین تفاوت پیدا شده: کاراکتر، شماره خط، بایت ها، و مقادیر آنها:

`cmp --print-bytes `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">مسیر/به/فایل_اول</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">مسیر/به/فایل_دوم</span>

- نمایش شماره بایتها و مقادیر تمامی تفاوت ها:

`cmp --verbose `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">مسیر/به/فایل_اول</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">مسیر/به/فایل_دوم</span>

- مقایسه فایلها در حالت خاموش، تنها مقدار خروجی برنامه در ترمینال در دسترس است:

`cmp --quiet `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">مسیر/به/فایل_اول</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">مسیر/به/فایل_دوم</span>
