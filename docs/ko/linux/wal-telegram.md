---
layout: page
title: linux/wal-telegram (한국어)
description: "pywal/wal이 생성한 색상을 기반으로 Telegram 테마를 생성."
content_hash: d26ac6897d95608cbc7a77dde7b67f10c6ac69b6
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/linux/wal-telegram.html
    icon: bi bi-globe
tldri18n_status: 2
---
# wal-telegram

pywal/wal이 생성한 색상을 기반으로 Telegram 테마를 생성.
더 많은 정보: <https://github.com/guillaumeboehm/wal-telegram>.

- wal의 팔레트와 현재 배경화면(feh 전용)으로 생성:

`wal-telegram`

- wal의 팔레트와 지정된 배경 이미지로 생성:

`wal-telegram --background=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지</span>

- wal의 팔레트와 팔레트를 기반으로 한 색상 배경으로 생성:

`wal-telegram --tiled`

- 배경 이미지에 가우시안 블러 적용:

`wal-telegram -g`

- 생성된 테마의 저장 위치 지정(기본값은 `$XDG_CACHE_HOME/wal-telegram` 또는 `~/.cache/wal-telegram`):

`wal-telegram --destination=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/저장소</span>

- 생성 후 Telegram 앱 재시작:

`wal-telegram --restart`
