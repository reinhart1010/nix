---
layout: page
title: common/pactl (한국어)
description: "실행 중인 PulseAudio 사운드 서버 제어."
content_hash: b5af92b40fe46381171dc25cd951e9a5c9067d78
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/common/pactl.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/pactl.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pactl

실행 중인 PulseAudio 사운드 서버 제어.
더 많은 정보: <https://manned.org/pactl>.

- 사운드 서버 정보 표시:

`pactl info`

- 모든 싱크(또는 다른 유형 - 싱크는 출력이고 싱크 입력은 활성 오디오 스트림) 나열:

`pactl list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sinks</span>` short`

- 기본 싱크(출력)를 1로 변경 (번호는 `list` 하위 명령을 통해 확인 가능):

`pactl set-default-sink `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1</span>

- 싱크 입력 627을 싱크 1로 이동:

`pactl move-sink-input `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">627</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1</span>

- 싱크 1의 볼륨을 75%로 설정:

`pactl set-sink-volume `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0.75</span>

- 기본 싱크의 음소거 전환 (특수 이름 `@DEFAULT_SINK@` 사용):

`pactl set-sink-mute `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">@DEFAULT_SINK@</span>` toggle`
