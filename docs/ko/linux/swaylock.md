---
layout: page
title: linux/swaylock (한국어)
description: "Wayland 컴포지터용 화면 잠금 도구."
content_hash: 838e48260e6fb353761a4c4ef098f59c5ff132a4
last_modified_at: 2024-11-12
related_topics:
  - title: English version
    url: /en/linux/swaylock.html
    icon: bi bi-globe
tldri18n_status: 2
---
# swaylock

Wayland 컴포지터용 화면 잠금 도구.
더 많은 정보: <https://manned.org/swaylock>.

- 흰색 배경으로 화면 잠금:

`swaylock`

- 단색 배경으로 화면 잠금 (rrggbb 형식):

`swaylock --color `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0000ff</span>

- PNG 배경 이미지로 화면 잠금:

`swaylock --image `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.png</span>

- 잠금 해제 표시기를 비활성화하고 화면 잠금 (키 입력 시 피드백 제거):

`swaylock --no-unlock-indicator`

- 마우스 포인터를 숨기지 않고 화면 잠금:

`swaylock --pointer `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">default</span>

- 모든 모니터에 타일 형식으로 PNG 배경 이미지로 화면 잠금:

`swaylock --image `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.png</span>` --tiling`

- 실패한 로그인 시도 횟수를 표시하며 화면 잠금:

`swaylock --show-failed-attempts`

- 파일에서 설정 불러오기:

`swaylock --config `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/설정</span>
