---
layout: page
title: common/ppmtoilbm (한국어)
description: "PPM 이미지를 ILBM 파일로 변환."
content_hash: eaa0804923f9ad4bbac3fcac50898aef27733f43
last_modified_at: 2024-11-06
related_topics:
  - title: English version
    url: /en/common/ppmtoilbm.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ppmtoilbm

PPM 이미지를 ILBM 파일로 변환.
더 많은 정보: <https://netpbm.sourceforge.net/doc/ppmtoilbm.html>.

- PPM 이미지를 ILBM 파일로 변환:

`ppmtoilbm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.ppm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.ilbm</span>

- ILBM 파일에 최대 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">n</span>`개의 플레인 작성하고, 이 수를 초과하면 HAM/24비트/직접 색상 파일 생성:

`ppmtoilbm -maxplanes `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">n</span>` -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hamif|24if|dcif</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.ppm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.ilbm</span>

- 정확히 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">n</span>`개의 플레인으로 ILBM 파일 생성:

`ppmtoilbm -fixplanes `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">n</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.ppm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.ilbm</span>

- 사용할 압축 방법 선택:

`ppmtoilbm -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">compress|nocompress|savemem</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.ppm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.ilbm</span>
