---
layout: page
title: common/bw (한국어)
description: "Bitwarden 보관함에 접속과 관리를 위한 CLI."
content_hash: 4ba20ec11050208f8dedd2f5d6ea3cb5b6ae8cc7
related_topics:
  - title: English version
    url: /en/common/bw.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/bw.html
    icon: bi bi-globe
---
# bw

Bitwarden 보관함에 접속과 관리를 위한 CLI.
더 많은 정보: <https://help.bitwarden.com/article/cli/>.

- Bitwarden 사용자 계정 로그인:

`bw login`

- 사용자 계정 로그아웃:

`bw logout`

- Bitwarden 보관함으로부터 아이템 검색과 출력:

`bw list items --search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">github</span>

- Bitwarden 보관함으로부터 특정 아이템 출력:

`bw get item `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">github</span>

- Bitwarden 보관함에 폴더 생성:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">echo -n '{"name":"My Folder1"}' | base64</span>` | bw create folder`
