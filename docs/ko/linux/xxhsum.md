---
layout: page
title: linux/xxhsum (한국어)
description: "빠른 비암호화 알고리즘인 xxHash를 사용하여 체크섬을 출력하거나 검증합니다."
content_hash: ab92833965af16412844fe240f225d55058a2253
last_modified_at: 2024-11-11
related_topics:
  - title: English version
    url: /en/linux/xxhsum.html
    icon: bi bi-globe
tldri18n_status: 2
---
# xxhsum

빠른 비암호화 알고리즘인 xxHash를 사용하여 체크섬을 출력하거나 검증합니다.
더 많은 정보: <https://github.com/Cyan4973/xxHash>.

- 특정 알고리즘을 사용하여 [f]파일의 체크섬 계산:

`xxhsum -H`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0|32|64|128</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 벤치마크 실행:

`xxhsum -b`
