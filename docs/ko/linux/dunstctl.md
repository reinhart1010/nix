---
layout: page
title: linux/dunstctl (한국어)
description: "`dunst` 제어 명령어."
content_hash: c89de965e8051cb502f151ed94d92f2884e05ac8
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/linux/dunstctl.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/dunstctl.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># dunstctl

`dunst` 제어 명령어.
더 많은 정보: <https://manned.org/dunstctl>.

- 알림 일시 중지:

`dunstctl set-paused true`

- 알림 일시 중지 해제:

`dunstctl set-paused false`

- 모든 알림 닫기:

`dunstctl close-all`

- 도움말 표시:

`dunstctl --help`
