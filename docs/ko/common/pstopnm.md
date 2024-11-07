---
layout: page
title: common/pstopnm (한국어)
description: "PostScript 파일을 PNM 이미지로 변환."
content_hash: dba9237818be6e209987a247d7fd86b3d47bcfa9
last_modified_at: 2024-11-07
related_topics:
  - title: English version
    url: /en/common/pstopnm.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/pstopnm.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># pstopnm

PostScript 파일을 PNM 이미지로 변환.
더 많은 정보: <https://netpbm.sourceforge.net/doc/pstopnm.html>.

- PS 파일을 PNM 이미지로 변환하고 입력의 페이지 N을 `path/to/fileN.ppm`에 저장:

`pstopnm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.ps</span>

- 출력 형식 명시적으로 지정:

`pstopnm -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pbm|pgm|ppm</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.ps</span>

- 출력 해상도를 인치당 도트로 지정:

`pstopnm -dpi `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">n</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.ps</span>
