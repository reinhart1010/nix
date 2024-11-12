---
layout: page
title: linux/swww (한국어)
description: "Wayland용 효율적인 애니메이션 배경화면 데몬."
content_hash: a7a2fe4c75922347e1c64e475f718a3f9ef140f4
last_modified_at: 2024-11-12
related_topics:
  - title: English version
    url: /en/linux/swww.html
    icon: bi bi-globe
tldri18n_status: 2
---
# swww

Wayland용 효율적인 애니메이션 배경화면 데몬.
같이 보기: `swww-daemon`.
더 많은 정보: <https://github.com/LGFae/swww>.

- 배경화면 설정:

`swww img `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지</span>

- 지정한 [o]출력에 배경화면 설정:

`swww img -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">출력1,출력2,...</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지</span>

- 마지막 배경화면 복원:

`swww restore`

- 데몬 종료:

`swww kill`

- 출력 정보 표시:

`swww query`
