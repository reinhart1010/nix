---
layout: page
title: common/ppmtomitsu (한국어)
description: "PPM 이미지를 Mitsubishi S340-10 파일로 변환."
content_hash: 2953231217b21f7b2e9134d1be40db751978453d
last_modified_at: 2024-11-06
related_topics:
  - title: English version
    url: /en/common/ppmtomitsu.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ppmtomitsu

PPM 이미지를 Mitsubishi S340-10 파일로 변환.
더 많은 정보: <https://netpbm.sourceforge.net/doc/ppmtomitsu.html>.

- PPM 이미지를 MITSU 파일로 변환:

`ppmtomitsu `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.ppm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.mitsu</span>

- 이미지를 지정된 배율로 확대하고, 지정된 선명도를 사용하여 `n`개의 복사본 생성:

`ppmtomitsu -enlarge `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1|2|3</span>` -sharpness `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1|2|3|4</span>` -copy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">n</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.ppm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.mitsu</span>

- 인쇄 과정에 주어진 매체 사용:

`ppmtomitsu -media `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">A|A4|AS|A4S</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.ppm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.mitsu</span>
