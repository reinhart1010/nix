---
layout: page
title: common/bvnc (한국어)
description: "로컬 네트워크에서 SSH/VNC 서버를 검색하기 위한 GUI 도구."
content_hash: 82ed25e331b51e682cdff00e556171f5724a6319
last_modified_at: 2024-09-27
related_topics:
  - title: English version
    url: /en/common/bvnc.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/bvnc.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># bvnc

로컬 네트워크에서 SSH/VNC 서버를 검색하기 위한 GUI 도구.
참고: `bssh` 및 `bshell`.
더 많은 정보: <https://manned.org/bvnc>.

- VNC 서버 탐색:

`bvnc`

- SSH 서버 탐색:

`bvnc --ssh`

- VNC 및 SSH 서버 탐색:

`bvnc --shell`

- 지정된 도메인에서 VNC 서버를 찾음:

`bvnc --domain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">도메인</span>
