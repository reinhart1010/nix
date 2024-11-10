---
layout: page
title: linux/plasmashell (한국어)
description: "Plasma 데스크톱을 시작하고 재시작합니다."
content_hash: 82a809d9cff8e60f98a9170ad2045d5fe9568868
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/linux/plasmashell.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/plasmashell.html
    icon: bi bi-globe
tldri18n_status: 2
---
# plasmashell

Plasma 데스크톱을 시작하고 재시작합니다.
더 많은 정보: <https://invent.kde.org/plasma/plasma-desktop>.

- `plasmashell` 재시작:

`systemctl restart --user plasma-plasmashell`

- systemd 없이 `plasmashell` 재시작:

`plasmashell --replace & disown`

- 명령줄 옵션에 대한 [h]도움말 표시:

`plasmashell --help`

- Qt 옵션을 포함한 도움말 표시:

`plasmashell --help-all`
