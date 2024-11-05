---
layout: page
title: common/xpmtoppm (한국어)
description: "X11 픽스맵을 PPM 이미지로 변환."
content_hash: d3af33ab27a26a9b083f651d3af07d8fdcd93d71
last_modified_at: 2024-11-05
related_topics:
  - title: English version
    url: /en/common/xpmtoppm.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/xpmtoppm.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># xpmtoppm

X11 픽스맵을 PPM 이미지로 변환.
더 많은 정보: <https://netpbm.sourceforge.net/doc/xpmtoppm.html>.

- XPM 이미지를 PPM 이미지로 변환:

`xpmtoppm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력_파일.xpm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력_파일.ppm</span>

- 입력 이미지의 투명 마스크를 지정된 파일에 저장:

`xpmtoppm --alphaout `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/알파_파일.pbm</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력_파일.xpm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력_파일.ppm</span>
