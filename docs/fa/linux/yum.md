---
layout: page
title: linux/yum (فارسی)
description: "ابزار مدیریت بسته برای ردهت، فدورا و سنت اواس(برای نسخه های قدیمی)."
content_hash: d6f1ab1e2cdb6f4ecb76de0344ec2277ff2c996b
last_modified_at: 2023-11-12
related_topics:
  - title: català version
    url: /ca/linux/yum.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/yum.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/yum.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/linux/yum.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/yum.html
    icon: bi bi-globe
tldri18n_status: 2
---
# yum

ابزار مدیریت بسته برای ردهت، فدورا و سنت اواس(برای نسخه های قدیمی).
اطلاعات بیشتر: <https://manned.org/yum>.

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
