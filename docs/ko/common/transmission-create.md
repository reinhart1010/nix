---
layout: page
title: common/transmission-create (한국어)
description: "BitTorrent `.torrent` 파일 만들기."
content_hash: 4f3e720611e7a0a1206a0346c37d33ed018c817a
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/common/transmission-create.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/transmission-create.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/transmission-create.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/transmission-create.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># transmission-create

BitTorrent `.torrent` 파일 만들기.
같이 보기: `transmission`.
더 많은 정보: <https://manned.org/transmission-create>.

- 2048 KB를 조각 크기로 하여 토렌트 생성:

`transmission-create -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/example.torrent</span>` --tracker `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">트래커_발표_URL</span>` --piecesize `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2048</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일_또는_폴더</span>

- 2048 KB 조각 크기로 개인 토렌트 생성:

`transmission-create -p -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/example.torrent</span>` --tracker `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">트래커_발표_URL</span>` --piecesize `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2048</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일_또는_폴더</span>

- 코멘트를 포함하여 토렌트 생성:

`transmission-create -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/example.torrent</span>` --tracker `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">트래커_URL1</span>` -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">코멘트</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일_또는_폴더</span>

- 여러 트래커를 포함하여 토렌트 생성:

`transmission-create -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/example.torrent</span>` --tracker `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">트래커_URL1</span>` --tracker `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">트래커_URL2</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일_또는_폴더</span>

- 도움말 페이지 표시:

`transmission-create --help`
