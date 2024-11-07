---
layout: page
title: common/rtl_sdr (한국어)
description: "RTL-SDR 수신기를 위한 원시 데이터 기록기."
content_hash: 7133c7a26a7374f8af4cc0b255dea4b5f4d81eb1
last_modified_at: 2024-11-07
related_topics:
  - title: English version
    url: /en/common/rtl_sdr.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/rtl_sdr.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># rtl_sdr

RTL-SDR 수신기를 위한 원시 데이터 기록기.
데이터는 I/Q 샘플링(즉, 직교 샘플링)을 사용하여 인코딩됩니다.
더 많은 정보: <https://osmocom.org/projects/rtl-sdr/wiki/Rtl-sdr>.

- 주파수(Hz 단위로 지정)에서 RAW 데이터를 파일로 저장:

`rtl_sdr -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">100000000</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 데이터를 다른 프로그램으로 파이프 처리:

`rtl_sdr -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">100000000</span>` - | `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">aplay</span>

- 지정된 수의 샘플 읽기:

`rtl_sdr -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">100000000</span>` -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">20</span>` -`

- 샘플 속도를 Hz 단위로 지정 (범위 225001-300000 및 900001-3200000):

`rtl_sdr -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">100000000</span>` -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2400000</span>` -`

- 인덱스로 디바이스 지정:

`rtl_sdr -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">100000000</span>` -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0</span>` -`

- 이득(gain) 지정:

`rtl_sdr -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">100000000</span>` -g `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">20</span>` -`

- 출력 블록 크기 지정:

`rtl_sdr -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">100000000</span>` -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">9999999</span>` -`

- 동기 출력 사용:

`rtl_sdr -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">100000000</span>` -S -`
