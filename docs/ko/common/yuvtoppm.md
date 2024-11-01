---
layout: page
title: common/yuvtoppm (한국어)
description: "Abekas YUV 바이트를 PPM으로 변환."
content_hash: 685abe71c26cd9095af9041b22534abd85b342db
last_modified_at: 2024-11-01
related_topics:
  - title: English version
    url: /en/common/yuvtoppm.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/yuvtoppm.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># yuvtoppm

Abekas YUV 바이트를 PPM으로 변환.
더 많은 정보: <https://netpbm.sourceforge.net/doc/yuvtoppm.html>.

- 지정된 입력 파일에서 Akebas YUV 바이트를 읽고, 이를 PPM 이미지로 변환하여 지정된 출력 파일에 저장:

`yuvtoppm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">너비</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">높이</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력_파일.yuv</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력_파일.ppm</span>
