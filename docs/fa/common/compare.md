---
layout: page
title: common/compare (فارسی)
description: "ایجاد یک تصویر مقایسه ای برای مشخص کردن تفاوتهای دو عکس به صورت بصری."
content_hash: fbb4b94c186ceb8da2129086f39e20ed509d1c56
last_modified_at: 2024-01-09
related_topics:
  - title: Deutsch version
    url: /de/common/compare.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/compare.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/common/compare.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/compare.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># compare

ایجاد یک تصویر مقایسه ای برای مشخص کردن تفاوتهای دو عکس به صورت بصری.
بخشی از ImageMagick است.
اطلاعات بیشتر: <https://imagemagick.org/script/compare.php>.

- مقایسه دو عکس:

`compare `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image1.png</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image2.png</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/diff.png</span>

- مقایسه دو عکس با استفاده از معیار دلخواه:

`compare -verbose -metric `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">PSNR</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image1.png</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image2.png</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/diff.png</span>
