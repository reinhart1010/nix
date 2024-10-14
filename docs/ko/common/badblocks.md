---
layout: page
title: common/badblocks (한국어)
description: "장치에서 불량 블록을 검색."
content_hash: 18e3564a22e97bea3d1596db5a15ebb7532d5af0
last_modified_at: 2024-10-14
related_topics:
  - title: English version
    url: /en/common/badblocks.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/badblocks.html
    icon: bi bi-globe
tldri18n_status: 2
---
# badblocks

장치에서 불량 블록을 검색.
일부 불량 블록 사용은 파티션 테이블을 포함해 디스크의 모든 데이터를 지우는 등 돌이킬 수 없는 작업 유발 가능.
더 많은 정보: <https://manned.org/badblocks>.

- 비파괴 읽기 전용 테스트를 사용하여 디스크에서 불량 블록을 검색:

`sudo badblocks `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdX</span>

- 비파괴([n]on-destructive) 읽기-쓰기 테스트를 통해 마운트 해제된 디스크에서 불량 블록을 검색:

`sudo badblocks -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdX</span>

- 파괴적인 쓰기([w]rite) 테스트를 통해 마운트되지 않은 디스크에서 불량 블록을 검색:

`sudo badblocks -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdX</span>

- 파괴적인 쓰기([w]rite) 테스트를 사용하고 상세하게 진행([s]how [v]erbose):

`sudo badblocks -svw `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdX</span>

- 파괴적인 모드에선, 발견된 블록을 파일로 출력([o]utput):

`sudo badblocks -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>` -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdX</span>

- 4K 블록([b]lock) 크기 및 64K 블록 수([c]ount)를 사용하여 속도가 향상된 파괴 모드를 사용:

`sudo badblocks -w -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">4096</span>` -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">65536</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdX</span>
