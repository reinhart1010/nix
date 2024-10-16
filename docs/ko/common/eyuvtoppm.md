---
layout: page
title: common/eyuvtoppm (한국어)
description: "Berkeley YUV 파일을 PPM으로 변환."
content_hash: 24bddd43bec2c93464f493b4fab02dc36990cd2c
last_modified_at: 2024-10-16
related_topics:
  - title: English version
    url: /en/common/eyuvtoppm.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/eyuvtoppm.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># eyuvtoppm

Berkeley YUV 파일을 PPM으로 변환.
더 많은 정보: <https://netpbm.sourceforge.net/doc/eyuvtoppm.html>.

- 지정된 입력 파일에서 Berkeley YUV 파일을 읽고, 이를 PPM 이미지로 변환한 후 지정된 출력 파일에 저장:

`eyuvtoppm --width `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">너비</span>` --height `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">높이</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력_파일.eyuv</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력_파일.ppm</span>
