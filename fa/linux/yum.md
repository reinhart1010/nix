---
layout: page
title: linux/yum (فارسی)
description: "ابزار مدیریت بسته برای ردهت، فدورا و سنت اواس(برای نسخه های قدیمی)."
content_hash: a700801473c225e58c42d88ef89cb57f80149210
related_topics:
  - title: English version
    url: /en/linux/yum.html
    icon: bi bi-globe
---
# yum

ابزار مدیریت بسته برای ردهت، فدورا و سنت اواس(برای نسخه های قدیمی).
اطلاعات بیشتر: <https://man7.org/linux/man-pages/man8/yum.8.html>.

- نصب یک بسته:

`yum install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- نصب یک بسته با فرض بر اینکه پاسخ شما برای تمامی سوالات بله است(با گزینه update هم می توان از این روش استفاده کرد، مناسب برای به روز رسانی خودکار):

`yum -y install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- پیدا کردن بسته ای که دستور مورد نظر را فراهم می کند:

`yum provides `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>

- حذف یک بسته:

`yum remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- نمایش به روز رسانی ها برای بسته های نصب شده:

`yum check-update`

- به روز رسانی بسته های نصب شده به آخرین نسخه موجود:

`yum upgrade`
