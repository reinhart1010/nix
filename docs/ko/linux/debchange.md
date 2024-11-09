---
layout: page
title: linux/debchange (한국어)
description: "Debian 소스 패키지의 debian/changelog 파일을 관리합니다."
content_hash: 434bc416f183fc89009b1262c4b4b57b6ee06aad
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/debchange.html
    icon: bi bi-globe
tldri18n_status: 2
---
# debchange

Debian 소스 패키지의 debian/changelog 파일을 관리합니다.
더 많은 정보: <https://manned.org/debchange.1>.

- 비관리자 업로드를 위한 새 버전을 변경 로그에 추가:

`debchange --nmu`

- 현재 버전에 변경 로그 항목 추가:

`debchange --append`

- 지정된 ID의 버그를 종료하는 변경 로그 항목 추가:

`debchange --closes `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">버그_ID</span>
