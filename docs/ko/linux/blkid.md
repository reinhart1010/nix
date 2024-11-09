---
layout: page
title: linux/blkid (한국어)
description: "인식된 모든 파티션과 그에 대한 범용 고유 식별자(UUID)를 나열합니다."
content_hash: 7f85137b01c312f7cba886e9cb6555ecb54945ed
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/blkid.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/linux/blkid.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/blkid.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/blkid.html
    icon: bi bi-globe
tldri18n_status: 2
---
# blkid

인식된 모든 파티션과 그에 대한 범용 고유 식별자(UUID)를 나열합니다.
더 많은 정보: <https://manned.org/blkid>.

- 모든 파티션 나열:

`sudo blkid`

- 현재 마운트 지점을 포함하여 테이블 형식으로 모든 파티션 나열:

`sudo blkid -o list`
