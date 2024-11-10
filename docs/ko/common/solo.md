---
layout: page
title: common/solo (한국어)
description: "Solo 하드웨어 보안 키와 상호 작용."
content_hash: 03edae41f35d759c87712364c195ea3bc8fc769d
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/common/solo.html
    icon: bi bi-globe
tldri18n_status: 2
---
# solo

Solo 하드웨어 보안 키와 상호 작용.
더 많은 정보: <https://github.com/solokeys/solo-python>.

- 연결된 Solo 목록 표시:

`solo ls`

- 현재 연결된 Solo의 펌웨어를 최신 버전으로 업데이트:

`solo key update`

- 특정 Solo의 LED 깜빡이기:

`solo key wink --serial `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">일련_번호</span>

- 현재 연결된 Solo의 안전한 난수 생성기를 사용하여 무작위 바이트 생성:

`solo key rng raw`

- Solo의 직렬 출력 모니터링:

`solo monitor `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/직렬_포트</span>
