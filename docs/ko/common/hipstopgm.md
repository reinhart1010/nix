---
layout: page
title: common/hipstopgm (한국어)
description: "HIPS 파일을 입력으로 읽고 PGM 이미지를 출력으로 반환."
content_hash: 0cc4d51e0a867f0eb45eb2724b533e0d362a862a
last_modified_at: 2024-11-03
related_topics:
  - title: English version
    url: /en/common/hipstopgm.html
    icon: bi bi-globe
tldri18n_status: 2
---
# hipstopgm

HIPS 파일을 입력으로 읽고 PGM 이미지를 출력으로 반환.
HIPS 파일에 2개 이상의 프레임이 연속적으로 포함되어 있는 경우, `hipstopgm`은 모든 프레임을 수직으로 연결함.
더 많은 정보: <https://netpbm.sourceforge.net/doc/hipstopgm.html>.

- HIPS 파일을 PGM 이미지로 변환:

`hipstopgm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.hips</span>

- 모든 정보 메시지를 억제함:

`hipstopgm -quiet`

- 버전 정보 출력:

`hipstopgm -version`
