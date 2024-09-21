---
layout: page
title: common/bshell (한국어)
description: "로컬 네트워크에서 SSH/VNC 서버를 검색하기 위한 GUI."
content_hash: d5d99c8cee77197b8a34b8ea5253e5f212cc16bb
last_modified_at: 2024-09-21
related_topics:
  - title: English version
    url: /en/common/bshell.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/bshell.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># bshell

로컬 네트워크에서 SSH/VNC 서버를 검색하기 위한 GUI.
참고: `bssh` 및 `bvnc`.
더 많은 정보: <https://manned.org/bshell>.

- SSH 및 VNC 서버 모두 찾아보기:

`bshell`

- SSH 서버만 찾아보기:

`bshell --ssh`

- VNC 서버만 찾아보기:

`bshell --vnc`

- 지정된 도메인에서 SSH 및 VNC 서버를 모두 찾음:

`bshell --domain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">도메인</span>
