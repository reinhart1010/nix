---
layout: page
title: linux/playerctl (한국어)
description: "MPRIS를 통해 미디어 플레이어 제어."
content_hash: b4c3f0e1bf4d25984cfcf5d4cd64a6b25bb8ca5c
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/linux/playerctl.html
    icon: bi bi-globe
tldri18n_status: 2
---
# playerctl

MPRIS를 통해 미디어 플레이어 제어.
더 많은 정보: <https://github.com/altdesktop/playerctl>.

- 재생/일시정지 전환:

`playerctl play-pause`

- 다음 트랙으로 건너뛰기:

`playerctl next`

- 이전 트랙으로 돌아가기:

`playerctl previous`

- 모든 플레이어 나열:

`playerctl --list-all`

- 특정 플레이어에 명령 전송:

`playerctl --player `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">플레이어_이름</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">play-pause|next|previous|...</span>

- 모든 플레이어에 명령 전송:

`playerctl --all-players `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">play-pause|next|previous|...</span>

- 현재 트랙에 대한 메타데이터 표시:

`playerctl metadata --format "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">현재 재생 중: \{\{artist\}\} - \{\{album\}\} - \{\{title\}\}</span>`"`
