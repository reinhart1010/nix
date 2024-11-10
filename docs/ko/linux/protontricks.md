---
layout: page
title: linux/protontricks (한국어)
description: "Proton을 지원하는 게임을 위해 Winetricks 명령을 실행하는 간단한 래퍼."
content_hash: 64ef856ada0617dfbf696951d61f8d43c5cd4621
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/linux/protontricks.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/protontricks.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/linux/protontricks.html
    icon: bi bi-globe
tldri18n_status: 2
---
# protontricks

Proton을 지원하는 게임을 위해 Winetricks 명령을 실행하는 간단한 래퍼.
더 많은 정보: <https://github.com/Matoking/protontricks>.

- protontricks GUI 실행:

`protontricks --gui`

- 특정 게임에 대해 Winetricks 실행:

`protontricks `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">앱_ID</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">winetricks_인수</span>

- 게임 설치 디렉토리 내에서 명령 실행:

`protontricks -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">앱_ID</span>

- 설치된 모든 게임 [l]나열:

`protontricks -l`

- 게임의 이름으로 앱 ID [s]검색:

`protontricks -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">게임_이름</span>

- 도움말 표시:

`protontricks --help`
