---
layout: page
title: linux/nala (한국어)
description: "더 나은 형식의 패키지 관리 도구."
content_hash: 1472f23c4c3fff3343b0be0ff210e58c1cfc41b0
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/nala.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/linux/nala.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/nala.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># nala

더 나은 형식의 패키지 관리 도구.
`python-apt` API의 프론트엔드.
더 많은 정보: <https://gitlab.com/volian/nala>.

- 패키지를 설치하거나 최신 버전으로 업데이트:

`sudo nala install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>

- 패키지 제거:

`sudo nala remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>

- 패키지 및 설정 파일 제거:

`nala purge `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>

- 단어, 정규식(기본값) 또는 glob을 사용하여 패키지 이름 및 설명 검색:

`nala search "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패턴</span>`"`

- 사용 가능한 패키지 목록을 업데이트하고 시스템 업그레이드:

`sudo nala upgrade`

- 시스템에서 사용하지 않는 모든 패키지 및 의존성 제거:

`sudo nala autoremove`

- 다운로드 속도를 개선하기 위해 빠른 미러 가져오기:

`sudo nala fetch`

- 모든 거래 내역 표시:

`nala history`
