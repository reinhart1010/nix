---
layout: page
title: common/badblocks (한국어)
description: "불량 블록이 있는지 장치를 검사하십시오."
content_hash: 6833ce4f9acfb1e0d9450da8b882e637ace3e422
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/badblocks.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/badblocks.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># badblocks

불량 블록이 있는지 장치를 검사하십시오.
불량 블록을 사용하면 파티션 테이블을 포함하여 디스크의 모든 데이터를 지우는 등의 파괴적인 작업이 발생할 수 있습니다.
더 많은 정보: <https://manned.org/badblocks>.

- 비파괴 읽기 전용 테스트를 사용하여 디스크에서 불량 블록을 검사:

`sudo badblocks `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sda</span>

- 비파괴 읽기-쓰기 테스트로 마운트되지 않은 디스크에서 불량 블록이 있는지 검사:

`sudo badblocks -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sda</span>

- 파괴 쓰기 테스트로 마운드되지 않은 디스크에서 불량 블록이 있는지 검사:

`sudo badblocks -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sda</span>
