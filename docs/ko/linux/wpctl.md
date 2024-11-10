---
layout: page
title: linux/wpctl (한국어)
description: "WirePlumber를 관리하는 도구로, PipeWire의 세션 및 정책 관리자를 관리합니다."
content_hash: 4e91cd38780c62e5ad8f92b4c586e655e365c2a2
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/linux/wpctl.html
    icon: bi bi-globe
tldri18n_status: 2
---
# wpctl

WirePlumber를 관리하는 도구로, PipeWire의 세션 및 정책 관리자를 관리합니다.
참고: `id` 대신 특별한 이름인 `@DEFAULT_SINK@`을 사용하여 기본 싱크를 조작할 수 있습니다.
더 많은 정보: <https://pipewire.pages.freedesktop.org/wireplumber/>.

- WirePlumber가 관리하는 모든 객체 나열:

`wpctl status`

- 객체의 모든 속성 출력:

`wpctl inspect `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id</span>

- 객체를 해당 그룹의 기본값으로 설정:

`wpctl set-default `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id</span>

- 싱크의 볼륨 가져오기:

`wpctl get-volume `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id</span>

- 싱크의 볼륨을 `n` 퍼센트로 설정:

`wpctl set-volume `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">n</span>`%`

- 싱크의 볼륨을 `n` 퍼센트만큼 증가/감소:

`wpctl set-volume `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">n</span>`%`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">+|-</span>

- 싱크 음소거/음소거 해제 설정 (1은 음소거, 0은 음소거 해제):

`wpctl set-mute `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1|0|toggle</span>
