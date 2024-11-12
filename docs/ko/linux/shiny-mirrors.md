---
layout: page
title: linux/shiny-mirrors (한국어)
description: "Manjaro Linux용 `pacman` 미러 목록 생성."
content_hash: 3d58a5521915e33dbf96275ec208130e49e5ce09
last_modified_at: 2024-11-12
related_topics:
  - title: English version
    url: /en/linux/shiny-mirrors.html
    icon: bi bi-globe
tldri18n_status: 2
---
# shiny-mirrors

Manjaro Linux용 `pacman` 미러 목록 생성.
shiny-mirrors를 실행할 때마다 `sudo pacman -Syyu` 명령어로 데이터베이스를 동기화하고 시스템을 업데이트해야 합니다.
더 많은 정보: <https://gitlab.com/Arisa_Snowbell/shiny-mirrors/-/blob/domina/shiny-mirrors/man/shiny-mirrors.md>.

- 현재 미러 상태 확인:

`shiny-mirrors status`

- 기본 동작으로 미러 목록 생성:

`sudo shiny-mirrors refresh`

- 현재 구성 파일 표시:

`shiny-mirrors config show`

- 다른 브랜치로 대화식 전환:

`sudo shiny-mirrors config --branch`
