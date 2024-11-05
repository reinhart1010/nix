---
layout: page
title: common/ppmtospu (한국어)
description: "PPM 파일을 Atari Spectrum 512 이미지로 변환."
content_hash: 1ceb5b50a4434bd72c4a455b660ddfd7ced701ff
last_modified_at: 2024-11-05
related_topics:
  - title: English version
    url: /en/common/ppmtospu.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/ppmtospu.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># ppmtospu

PPM 파일을 Atari Spectrum 512 이미지로 변환.
더 많은 정보: <https://netpbm.sourceforge.net/doc/ppmtospu.html>.

- PPM 파일을 Atari Spectrum 512 이미지로 변환:

`ppmtospu `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력.ppm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.spu</span>

- 지정된 크기의 디더링 매트릭스를 사용 (0은 디더링 없음):

`ppmtospu -d`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0|2|4</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력.ppm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.spu</span>
