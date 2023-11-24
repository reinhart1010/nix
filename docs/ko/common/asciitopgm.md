---
layout: page
title: common/asciitopgm (한국어)
description: "ASCII 그래픽을 PGM 파일로 변환합니다."
content_hash: 2f5be297d6f9a512b45f5293e0aa4a1bf2175960
last_modified_at: 2023-11-24
related_topics:
  - title: English version
    url: /en/common/asciitopgm.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/asciitopgm.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># asciitopgm

ASCII 그래픽을 PGM 파일로 변환합니다.
더 많은 정보: <https://netpbm.sourceforge.net/doc/asciitopgm.html>.

- ASCII 데이터를 입력으로 읽고 ASCII 문자의 "밝기"에 가까운 픽셀 값을 사용하여 PGM 이미지를 생성:

`asciitopgm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력_파일</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력_파일.pgm</span>

- 버전 정보 표시:

`asciitopgm -version`
