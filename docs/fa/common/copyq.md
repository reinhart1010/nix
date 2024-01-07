---
layout: page
title: common/copyq (فارسی)
description: "مدیریت کلیپ بورد با قابلیت های پیشرفته."
content_hash: f61e193481cca82f6832ee3224e21226eaa79016
last_modified_at: 2024-01-07
related_topics:
  - title: English version
    url: /en/common/copyq.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/copyq.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/copyq.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># copyq

مدیریت کلیپ بورد با قابلیت های پیشرفته.
اطلاعات بیشتر: <https://copyq.readthedocs.io/en/latest/command-line.html>.

- اجرای کپی کیو برای ذخیره تاریخچه کلیپ بورد:

`copyq`

- نمایش محتوای کنونی کلیپ بورد:

`copyq clipboard`

- وارد کردن متن خام به تاریخچه کلیپ بورد:

`copyq add -- `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">text1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">text2</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">text3</span>

- وارد کردن متن شامل رشته های فاصله انداز مانند (\n, \t) در تاریخچه کلیپ بورد:

`copyq add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">firstline\nsecondline</span>

- چاپ محتوای سه مورد اول در تاریخچه کلیپ بورد:

`copyq read 0 1 2`

- رونوشت محتوای یک فایل در کلیپ بورد:

`copyq copy < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.txt</span>

- رونوشت یک عکس با فرمت JPEG در کلیپ بورد:

`copyq copy image/jpeg < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image.jpg</span>
