---
layout: page
title: linux/updatedb (한국어)
description: "`locate`에서 사용하는 데이터베이스를 생성하거나 업데이트."
content_hash: 6252d53fee4325adc08472c5b7d87b956c602c40
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/linux/updatedb.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/updatedb.html
    icon: bi bi-globe
tldri18n_status: 2
---
# updatedb

`locate`에서 사용하는 데이터베이스를 생성하거나 업데이트.
일반적으로 cron에 의해 일일 실행.
더 많은 정보: <https://manned.org/updatedb>.

- 데이터베이스 내용 새로고침:

`sudo updatedb`

- 파일 이름을 찾는 즉시 표시:

`sudo updatedb --verbose`
