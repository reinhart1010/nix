---
layout: page
title: linux/mkfs.xfs (한국어)
description: "파티션 내에 XFS 파일 시스템 생성."
content_hash: 91e501a2e95d6103d598b4e947a084db3f6566af
last_modified_at: 2024-10-15
related_topics:
  - title: English version
    url: /en/linux/mkfs.xfs.html
    icon: bi bi-globe
tldri18n_status: 2
---
# mkfs.xfs

파티션 내에 XFS 파일 시스템 생성.
더 많은 정보: <https://manned.org/mkfs.xfs>.

- 장치의 파티션 1에 XFS 파일 시스템 생성:

`sudo mkfs.xfs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdX1</span>

- 볼륨 레이블을 사용하여 XFS 파일 시스템 생성:

`sudo mkfs.xfs -L `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">볼륨_레이블</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdX1</span>
