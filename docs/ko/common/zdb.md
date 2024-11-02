---
layout: page
title: common/zdb (한국어)
description: "ZFS 디버거."
content_hash: 1868a78d7c0af54a6f90d6a254ecf74adea7c44a
last_modified_at: 2024-11-02
related_topics:
  - title: English version
    url: /en/common/zdb.html
    icon: bi bi-globe
tldri18n_status: 2
---
# zdb

ZFS 디버거.
더 많은 정보: <https://manned.org/zdb>.

- 모든 마운트된 ZFS zpool의 상세 설정 보기:

`zdb`

- 특정 ZFS 풀의 상세 설정 보기:

`zdb -C `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">풀명</span>

- 블록의 수, 크기 및 중복 제거에 대한 통계 보기:

`zdb -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">풀명</span>
