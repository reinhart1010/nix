---
layout: page
title: common/ulimit (한국어)
description: "사용자 제한을 조회하고 설정."
content_hash: fa829a7f165bba8dd615028df7312aa6d74b6323
last_modified_at: 2024-11-02
related_topics:
  - title: English version
    url: /en/common/ulimit.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ulimit

사용자 제한을 조회하고 설정.
더 많은 정보: <https://manned.org/ulimit>.

- 모든 사용자 제한의 속성 조회:

`ulimit -a`

- 동시에 열 수 있는 파일 개수의 하드 제한 조회:

`ulimit -H -n`

- 동시에 열 수 있는 파일 개수의 소프트 제한 조회:

`ulimit -S -n`

- 사용자별 프로세스 최대 개수 설정:

`ulimit -u 30`
