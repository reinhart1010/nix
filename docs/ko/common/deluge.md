---
layout: page
title: common/deluge (한국어)
description: "BitTorrent 클라이언트 명령어."
content_hash: 201e90299b66c0d7aa8f835e70544060337e75b9
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/deluge.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/deluge.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/deluge.html
    icon: bi bi-globe
tldri18n_status: 2
---
# deluge

BitTorrent 클라이언트 명령어.
더 많은 정보: <https://deluge-torrent.org>.

- 토렌트 다운로드:

`deluge `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url|마그넷|경로/파일명</span>

- 특정 구성 파일을 사용하여 토렌트를 다운로드하십시오:

`deluge -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/구성_파일</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url|마그넷|경로/파일명</span>

- 토렌트를 다운로드하고 지정된 사용자 인터페이스로 시작:

`deluge -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gtk|웹|콘솔</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url|마그넷|경로/파일명</span>

- 토렌트를 다운로드하고 로그를 파일로 출력:

`deluge -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/로그_파일</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url|마그넷|경로/파일명</span>
