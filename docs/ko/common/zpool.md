---
layout: page
title: common/zpool (한국어)
description: "ZFS 풀 관리."
content_hash: 4ea61e5807ea47f1ac545709bb8d6b4f3ada3256
last_modified_at: 2024-11-02
related_topics:
  - title: English version
    url: /en/common/zpool.html
    icon: bi bi-globe
tldri18n_status: 2
---
# zpool

ZFS 풀 관리.
더 많은 정보: <https://manned.org/zpool>.

- 모든 ZFS 풀의 구성 및 상태 표시:

`zpool status`

- ZFS 풀에서 오류 검사 (모든 블록의 체크섬 검증). 매우 높은 CPU 및 디스크 사용량:

`zpool scrub `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">풀_이름</span>

- 가져올 수 있는 ZFS 풀 목록:

`zpool import`

- ZFS 풀 가져오기:

`zpool import `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">풀_이름</span>

- ZFS 풀 내보내기 (모든 파일 시스템 마운트 해제):

`zpool export `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">풀_이름</span>

- 모든 풀 작업의 기록 표시:

`zpool history `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">풀_이름</span>

- 미러링된 풀 생성:

`zpool create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">풀_이름</span>` mirror `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">디스크1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">디스크2</span>` mirror `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">디스크3</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">디스크4</span>

- ZFS 풀에 캐시 (L2ARC) 장치 추가:

`zpool add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">풀_이름</span>` cache `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">캐시_디스크</span>
