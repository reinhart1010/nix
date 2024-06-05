---
layout: page
title: common/magick-compare (فارسی)
description: "ایجاد یک تصویر مقایسه ای برای مشخص کردن تفاوتهای دو عکس به صورت بصری."
content_hash: 871bee72ef154e0a3df8268a44b06f44a2d31eb1
last_modified_at: 2024-06-05
related_topics:
  - title: Deutsch version
    url: /de/common/magick-compare.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/magick-compare.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/common/magick-compare.html
    icon: bi bi-globe
tldri18n_status: 2
---
# magick compare

ایجاد یک تصویر مقایسه ای برای مشخص کردن تفاوتهای دو عکس به صورت بصری.
بخشی از ImageMagick است.
اطلاعات بیشتر: <https://imagemagick.org/script/compare.php>.

- مقایسه دو عکس:

`magick compare `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image1.png</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image2.png</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/diff.png</span>

- مقایسه دو عکس با استفاده از معیار دلخواه:

`magick compare -verbose -metric `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">PSNR</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image1.png</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image2.png</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/diff.png</span>
