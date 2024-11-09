---
layout: page
title: linux/plasmashell (한국어)
description: "Plasma 데스크톱을 시작하고 재시작합니다."
content_hash: 82a809d9cff8e60f98a9170ad2045d5fe9568868
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/plasmashell.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/plasmashell.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/plasmashell.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># plasmashell

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
