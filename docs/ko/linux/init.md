---
layout: page
title: linux/init (한국어)
description: "Linux 런레벨 관리자."
content_hash: eed25230806eec2fa48559ac9e49cc627223fa2e
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/linux/init.html
    icon: bi bi-globe
tldri18n_status: 2
---
# init

Linux 런레벨 관리자.
systemd를 사용하는 경우 SYSVINIT 컴파일 시 옵션이 활성화되어야 합니다.
더 많은 정보: <https://manned.org/man/init.8>.

- 시스템을 그래픽 환경으로 설정:

`sudo init 5`

- 시스템을 다중 사용자 터미널로 설정:

`sudo init 3`

- 시스템 종료:

`init 0`

- 시스템 재부팅:

`init 6`

- 루트 사용자만 허용되고 네트워킹이 없는 터미널로 시스템 설정:

`sudo init 1`
