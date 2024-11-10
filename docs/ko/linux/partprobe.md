---
layout: page
title: linux/partprobe (한국어)
description: "운영 체제 커널에 파티션 테이블 변경 사항을 알립니다."
content_hash: eba0f1336557711686dfc2db7aa448470243b99a
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/linux/partprobe.html
    icon: bi bi-globe
tldri18n_status: 2
---
# partprobe

운영 체제 커널에 파티션 테이블 변경 사항을 알립니다.
더 많은 정보: <https://manned.org/partprobe>.

- 운영 체제 커널에 파티션 테이블 변경 사항 알림:

`sudo partprobe`

- 커널에 파티션 테이블 변경 사항을 알리고 장치 및 해당 파티션의 요약 표시:

`sudo partprobe --summary`

- 커널에 알리지 않고 장치 및 해당 파티션의 요약 표시:

`sudo partprobe --summary --dry-run`
