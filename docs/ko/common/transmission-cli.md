---
layout: page
title: common/transmission-cli (한국어)
description: "경량의 명령줄 기반 BitTorrent 클라이언트."
content_hash: 33ff68fb3d841b9562da475aef532a730defe44b
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/common/transmission-cli.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/transmission-cli.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/transmission-cli.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/transmission-cli.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># transmission-cli

경량의 명령줄 기반 BitTorrent 클라이언트.
이 도구는 사용이 중단되었습니다. `transmission-remote`를 참조하세요.
더 많은 정보: <https://transmissionbt.com>.

- 특정 토렌트 다운로드:

`transmission-cli `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url|마그넷|경로/대상/파일</span>

- 특정 디렉토리에 토렌트 다운로드:

`transmission-cli --download-dir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/다운로드_디렉토리</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url|마그넷|경로/대상/파일</span>

- 특정 파일이나 디렉토리에서 토렌트 파일 생성:

`transmission-cli --new `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/소스_파일_또는_디렉토리</span>

- 다운로드 속도 제한 설정 (KB/s 단위):

`transmission-cli --downlimit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">50</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url|마그넷|경로/대상/파일</span>

- 업로드 속도 제한 설정 (KB/s 단위):

`transmission-cli --uplimit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">50</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url|마그넷|경로/대상/파일</span>

- 특정 포트를 사용하여 연결:

`transmission-cli --port `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">포트_번호</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url|마그넷|경로/대상/파일</span>

- 피어 연결에 암호화 강제 적용:

`transmission-cli --encryption-required `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url|마그넷|경로/대상/파일</span>

- Bluetack 형식의 피어 차단 목록 사용:

`transmission-cli --blocklist `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">차단목록_url|경로/대상/차단목록</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url|마그넷|경로/대상/파일</span>
