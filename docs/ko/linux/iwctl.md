---
layout: page
title: linux/iwctl (한국어)
description: "`iwd` 네트워크 서플리컨트를 제어합니다."
content_hash: dc1145a5a53c4418b9805c32e38270887c91c5c1
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/linux/iwctl.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/iwctl.html
    icon: bi bi-globe
tldri18n_status: 2
---
# iwctl

`iwd` 네트워크 서플리컨트를 제어합니다.
더 많은 정보: <https://archive.kernel.org/oldwiki/iwd.wiki.kernel.org/gettingstarted.html>.

- 대화형 모드 시작, 이 모드에서는 자동 완성 기능과 함께 명령어를 직접 입력할 수 있습니다:

`iwctl`

- 일반 도움말 호출:

`iwctl --help`

- Wi-Fi 스테이션 표시:

`iwctl station list`

- 스테이션으로 네트워크 검색 시작:

`iwctl station `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">스테이션</span>` scan`

- 스테이션에서 찾은 네트워크 표시:

`iwctl station `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">스테이션</span>` get-networks`

- 스테이션으로 네트워크에 연결, 자격 증명이 필요할 경우 요청받습니다:

`iwctl station `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">스테이션</span>` connect `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">네트워크_이름</span>
