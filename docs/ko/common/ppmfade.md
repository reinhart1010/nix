---
layout: page
title: common/ppmfade (한국어)
description: "두 개의 PPM 이미지 간의 전환을 생성."
content_hash: 36a3d8ae019003e781b020e3ca8ded6dd5297371
last_modified_at: 2024-11-05
related_topics:
  - title: English version
    url: /en/common/ppmfade.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/ppmfade.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># ppmfade

두 개의 PPM 이미지 간의 전환을 생성.
더 많은 정보: <https://netpbm.sourceforge.net/doc/ppmfade.html>.

- 지정된 효과를 사용하여 두 PPM 이미지([f]irst 및 [l]ast) 간의 전환 생성:

`ppmfade -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지1.ppm</span>` -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지2.ppm</span>` -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mix|spread|shift|relief|oil|...</span>

- 지정된 이미지로 시작하여 검은색 단색 이미지로 끝나는 전환 생성:

`ppmfade -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지.ppm</span>` -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mix|spread|shift|relief|oil|...</span>

- 검은색 단색 이미지로 시작하여 지정된 이미지로 끝나는 전환 생성:

`ppmfade -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지.ppm</span>` -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mix|spread|shift|relief|oil|...</span>

- 결과 이미지를 `base.NNNN.ppm` 형식의 파일에 저장 (`NNNN`은 증가하는 숫자):

`ppmfade -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지1.ppm</span>` -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지2.ppm</span>` -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mix|spread|shift|relief|oil|...</span>` -base `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">base</span>
