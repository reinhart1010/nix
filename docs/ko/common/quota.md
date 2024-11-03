---
layout: page
title: common/quota (한국어)
description: "사용자의 디스크 공간 사용량과 할당된 제한을 표시."
content_hash: 1a66743dfd30e2de88ff1a2bcb1d9e1a268178a8
last_modified_at: 2024-11-03
related_topics:
  - title: English version
    url: /en/common/quota.html
    icon: bi bi-globe
tldri18n_status: 2
---
# quota

사용자의 디스크 공간 사용량과 할당된 제한을 표시.
더 많은 정보: <https://manned.org/quota>.

- 현재 사용자의 디스크 할당량을 사람이 읽기 쉬운 단위로 표시:

`quota -s`

- 상세 출력 (저장 공간이 할당되지 않은 파일 시스템의 할당량도 표시):

`quota -v`

- 조용한 출력 (사용량이 할당량을 초과한 파일 시스템의 할당량만 표시):

`quota -q`

- 현재 사용자가 속한 그룹의 할당량 출력:

`quota -g`

- 다른 사용자의 디스크 할당량 표시:

`sudo quota -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자_명</span>
