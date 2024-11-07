---
layout: page
title: common/pcdovtoppm (한국어)
description: "사진 CD의 개요 파일을 기반으로 색인 이미지를 생성."
content_hash: b04c6420ccb960a11b550e25b413fc844a407d3d
last_modified_at: 2024-11-07
related_topics:
  - title: English version
    url: /en/common/pcdovtoppm.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/pcdovtoppm.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/pcdovtoppm.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/pcdovtoppm.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># pcdovtoppm

사진 CD의 개요 파일을 기반으로 색인 이미지를 생성.
더 많은 정보: <https://netpbm.sourceforge.net/doc/pcdovtoppm.html>.

- PCD 개요 파일에서 PPM 색인 이미지 생성:

`pcdovtoppm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.pcd</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.ppm</span>

- 출력 이미지의 최대 너비와 출력에 포함된 각 이미지의 최대 크기 지정:

`pcdovtoppm -m `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">너비</span>` -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">크기</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.pcd</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.ppm</span>

- 가로로 배치할 이미지의 최대 수와 최대 색상 수 지정:

`pcdovtoppm -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이미지_수</span>` -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">색상_수</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.pcd</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.ppm</span>

- 주석에 사용할 폰트를 지정하고 배경을 흰색으로 칠하기:

`pcdovtoppm -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">폰트</span>` -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.pcd</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.ppm</span>
