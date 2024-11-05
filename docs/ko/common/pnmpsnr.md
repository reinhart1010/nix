---
layout: page
title: common/pnmpsnr (한국어)
description: "두 이미지 간의 차이를 계산합니다."
content_hash: f90f29373edf80ce531d286801080f8c071edfc5
last_modified_at: 2024-11-05
related_topics:
  - title: English version
    url: /en/common/pnmpsnr.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/pnmpsnr.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/pnmpsnr.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># pnmpsnr

두 이미지 간의 차이를 계산합니다.
더 많은 정보: <https://netpbm.sourceforge.net/doc/pnmpsnr.html>.

- 두 이미지 간의 차이, 즉 피크 신호 대 잡음비(PSNR) 계산:

`pnmpsnr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일1.pnm</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일2.pnm</span>

- 이미지의 휘도 및 색도 성분 대신 색상 성분을 비교:

`pnmpsnr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일1.pnm</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일2.pnm</span>` -rgb`

- 비교 모드로 실행하여, 계산된 PSNR이 `n`을 초과하는지에 따라 `nomatch` 또는 `match`만 출력:

`pnmpsnr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일1.pnm</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일2.pnm</span>` -target `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">n</span>

- 비교 모드로 실행하고 개별 이미지 성분, 즉 Y, Cb 및 Cr을 해당 임계값과 비교:

`pnmpsnr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일1.pnm</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일2.pnm</span>` -target1 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">임계값_Y</span>` -target2 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">임계값_Cb</span>` -target3 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">임계값_Cr</span>

- 비교 모드로 실행하고 개별 이미지 성분, 즉 빨강, 초록, 파랑을 해당 임계값과 비교:

`pnmpsnr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일1.pnm</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일2.pnm</span>` -rgb -target1 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">임계값_빨강</span>` -target2 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">임계값_초록</span>` -target3 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">임계값_파랑</span>

- 기계가 읽을 수 있는 출력 생성:

`pnmpsnr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일1.pnm</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일2.pnm</span>` -machine`
