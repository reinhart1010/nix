---
layout: page
title: linux/distrobox-enter (한국어)
description: "Distrobox 컨테이너에 진입합니다. 같이 보기: `tldr distrobox`."
content_hash: e1ca15e4f6caa10932308d85f4fbdb70bb290ab4
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/distrobox-enter.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/distrobox-enter.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/distrobox-enter.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/linux/distrobox-enter.html
    icon: bi bi-globe
tldri18n_status: 2
---
# distrobox-enter

Distrobox 컨테이너에 진입합니다. 같이 보기: `tldr distrobox`.
기본 실행 명령어는 사용자의 SHELL이지만, 다른 셸 또는 전체 명령어를 지정하여 실행할 수 있습니다. 스크립트, 애플리케이션 또는 서비스 내에서 사용 시, `--headless` 모드를 사용하여 tty 및 상호작용을 비활성화할 수 있습니다.
더 많은 정보: <https://distrobox.it/usage/distrobox-enter>.

- Distrobox 컨테이너에 진입:

`distrobox-enter `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">컨테이너_이름</span>

- Distrobox 컨테이너에 진입하고 로그인 시 명령어 실행:

`distrobox-enter `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">컨테이너_이름</span>` -- `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sh -l</span>

- tty를 인스턴스화하지 않고 Distrobox 컨테이너에 진입:

`distrobox-enter --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">컨테이너_이름</span>` -- `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">uptime -p</span>
