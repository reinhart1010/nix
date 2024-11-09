---
layout: page
title: common/transmission-remote (한국어)
description: "`transmission-daemon` 및 `transmission`의 원격 제어 도구."
content_hash: 7edf3f9963ac6fef591316b21ac8ba51be495b52
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/common/transmission-remote.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/transmission-remote.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/transmission-remote.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/transmission-remote.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># transmission-remote

`transmission-daemon` 및 `transmission`의 원격 제어 도구.
더 많은 정보: <https://transmissionbt.com>.

- 토렌트 파일 또는 마그넷 링크를 Transmission에 추가하고 지정한 디렉토리로 다운로드:

`transmission-remote `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">호스트명</span>` -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">토렌트|url</span>` -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/경로/대상/다운로드_디렉토리</span>

- 기본 다운로드 디렉토리 변경:

`transmission-remote `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">호스트명</span>` -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/경로/대상/다운로드_디렉토리</span>

- 모든 토렌트 나열:

`transmission-remote `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">호스트명</span>` --list`

- 토렌트 1과 2 시작, 토렌트 3 중지:

`transmission-remote `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">호스트명</span>` -t "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1,2</span>`" --start -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3</span>` --stop`

- 토렌트 1과 2 제거, 토렌트 2의 로컬 데이터도 삭제:

`transmission-remote `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">호스트명</span>` -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1</span>` --remove -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2</span>` --remove-and-delete`

- 모든 토렌트 중지:

`transmission-remote `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">호스트명</span>` -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">all</span>` --stop`

- 토렌트 1-10 및 15-20을 새 디렉토리로 이동 (존재하지 않는 경우 생성됨):

`transmission-remote `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">호스트명</span>` -t "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1-10,15-20</span>`" --move `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/경로/대상/새_디렉토리</span>
