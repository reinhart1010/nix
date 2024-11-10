---
layout: page
title: linux/i3lock (한국어)
description: "i3 윈도우 관리자를 위해 만들어진 간단한 화면 잠금 도구."
content_hash: 7a337bf2d58605dc437bf51cb9c40b9ce433a512
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/linux/i3lock.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/i3lock.html
    icon: bi bi-globe
tldri18n_status: 2
---
# i3lock

i3 윈도우 관리자를 위해 만들어진 간단한 화면 잠금 도구.
더 많은 정보: <https://i3wm.org/i3lock>.

- 흰색 배경으로 화면 잠금:

`i3lock`

- 단색 배경(rrggbb 형식)으로 화면 잠금:

`i3lock --color `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0000ff</span>

- PNG 배경으로 화면 잠금:

`i3lock --image `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.png</span>

- 잠금 해제 표시기를 비활성화하고 화면 잠금 (키 입력 시 피드백 제거):

`i3lock --no-unlock-indicator`

- 마우스 포인터를 숨기지 않고 화면 잠금:

`i3lock --pointer `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">default</span>

- 모든 모니터에 타일링된 PNG 배경으로 화면 잠금:

`i3lock --image `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.png</span>` --tiling`

- 실패한 로그인 시도 횟수를 표시하며 화면 잠금:

`i3lock --show-failed-attempts`
