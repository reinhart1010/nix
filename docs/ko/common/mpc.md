---
layout: page
title: common/mpc (한국어)
description: "Music Player Client: Music Player Daemon (MPD)를 제어하는 클라이언트."
content_hash: 1ef2e2748e09636db91432006412dc7cd39e6f2a
last_modified_at: 2024-11-07
related_topics:
  - title: English version
    url: /en/common/mpc.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/mpc.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># mpc

Music Player Client: Music Player Daemon (MPD)를 제어하는 클라이언트.
같이 보기: `mpd`, `ncmpcpp`, `cmus`.
더 많은 정보: <https://www.musicpd.org/doc/mpc/html>.

- 재생/일시 정지 전환:

`mpc toggle`

- 재생 중지:

`mpc stop`

- 현재 재생 중인 곡에 대한 정보 표시:

`mpc status`

- 다음 곡 재생:

`mpc next`

- 이전 곡 재생:

`mpc prev`

- `n`초 앞으로(`+`) 또는 뒤로(`-`) 탐색:

`mpc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">+n|-n</span>
