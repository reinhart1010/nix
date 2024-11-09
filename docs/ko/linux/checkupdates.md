---
layout: page
title: linux/checkupdates (한국어)
description: "Arch Linux에서 보류 중인 업데이트를 확인합니다."
content_hash: ea324e33e539234323d70f3ff14f967557fd8651
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/checkupdates.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/linux/checkupdates.html
    icon: bi bi-globe
tldri18n_status: 2
---
# checkupdates

Arch Linux에서 보류 중인 업데이트를 확인합니다.
더 많은 정보: <https://manned.org/checkupdates.8>.

- 보류 중인 업데이트 나열:

`checkupdates`

- 보류 중인 업데이트를 나열하고 패키지를 `pacman` 캐시에 다운로드:

`checkupdates --download`

- 특정 `pacman` 데이터베이스를 사용하여 보류 중인 업데이트 나열:

`CHECKUPDATES_DB=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>` checkupdates`

- 도움말 표시:

`checkupdates --help`
