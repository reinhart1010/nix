---
layout: page
title: linux/flameshot (한국어)
description: "GUI가 있는 스크린샷 도구."
content_hash: dbe397ab4ef52ffb64aeb815c2cba3cce6333ef8
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/linux/flameshot.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/flameshot.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/flameshot.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/flameshot.html
    icon: bi bi-globe
tldri18n_status: 2
---
# flameshot

GUI가 있는 스크린샷 도구.
텍스트, 도형, 색상, imgur 같은 기본 이미지 편집을 지원합니다.
더 많은 정보: <https://flameshot.org>.

- 전체 화면 스크린샷 생성:

`flameshot full`

- 상호작용 방식으로 스크린샷 생성:

`flameshot gui`

- 특정 경로에 스크린샷 저장:

`flameshot gui --path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>

- 간소화된 모드로 상호작용 방식의 스크린샷 생성:

`flameshot launcher`

- 특정 모니터에서 스크린샷 생성:

`flameshot screen --number `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2</span>

- 스크린샷을 생성하고 `stdout`에 출력:

`flameshot gui --raw`

- 스크린샷을 생성하고 클립보드에 복사:

`flameshot gui --clipboard`

- 특정 밀리초 지연 후 스크린샷 생성:

`flameshot full --delay `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5000</span>
