---
layout: page
title: common/bssh (한국어)
description: "로컬 네트워크에서 SSH/VNC 서버를 검색하기 위한 GUI 도구."
content_hash: 28378be339e32cfe7440f729faa1a5e5d8f4ee34
last_modified_at: 2024-09-21
related_topics:
  - title: English version
    url: /en/common/bssh.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/bssh.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># bssh

로컬 네트워크에서 SSH/VNC 서버를 검색하기 위한 GUI 도구.
참고: `bvnc` 및 `bshell`.
더 많은 정보: <https://manned.org/bssh>.

- SSH 서버를 찾아보기:

`bssh`

- VNC 서버를 찾아보기:

`bssh --vnc`

- SSH 및 VNC 서버를 찾아보기:

`bssh --shell`

- 지정된 도메인에서 SSH 서버를 찾아보기:

`bssh --domain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">도메인</span>
