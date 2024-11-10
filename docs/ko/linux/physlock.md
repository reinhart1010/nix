---
layout: page
title: linux/physlock (한국어)
description: "모든 콘솔 및 가상 터미널을 잠급니다."
content_hash: f126c482143e2d3f0bfffe8230600f86c3e11496
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/linux/physlock.html
    icon: bi bi-globe
tldri18n_status: 2
---
# physlock

모든 콘솔 및 가상 터미널을 잠급니다.
더 많은 정보: <https://github.com/muennich/physlock>.

- 모든 콘솔 잠금 (해제하려면 현재 사용자 또는 root 필요):

`physlock`

- 잠금 동안 콘솔의 커널 메시지 음소거:

`physlock -m`

- 잠금 동안 SysRq 메커니즘 비활성화:

`physlock -s`

- 암호 입력 전 메시지 표시:

`physlock -p "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">잠겼습니다!</span>`"`

- physlock을 포크하고 분리 (일시 중지 또는 최대 절전 모드 스크립트에 유용):

`physlock -d`
