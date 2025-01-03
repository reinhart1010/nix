---
layout: page
title: common/tldr (한국어)
description: "tldr-pages 프로젝트에서 제공하는 명령줄 도구에 대한 간단한 도움말 페이지를 표시합니다."
content_hash: 1966277e51486a0e69fa2b08506a46fa772ea18f
last_modified_at: 2025-01-03
related_topics:
  - title: Deutsch version
    url: /de/common/tldr.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/tldr.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/tldr.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/tldr.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/common/tldr.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/tldr.html
    icon: bi bi-globe
  - title: ລາວ version
    url: /lo/common/tldr.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/tldr.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/tldr.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/tldr.html
    icon: bi bi-globe
  - title: sh version
    url: /sh/common/tldr.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/tldr.html
    icon: bi bi-globe
  - title: ไทย version
    url: /th/common/tldr.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/tldr.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/common/tldr.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/tldr.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/common/tldr.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># tldr

tldr-pages 프로젝트에서 제공하는 명령줄 도구에 대한 간단한 도움말 페이지를 표시합니다.
참고: `--language` 및 `--list` 옵션은 클라이언트 사양에 필수는 아니지만 대부분의 클라이언트가 이를 구현합니다.
더 많은 정보: <https://github.com/tldr-pages/tldr/blob/main/CLIENT-SPECIFICATION.md#command-line-interface>.

- 특정 명령에 대한 tldr 페이지를 출력 (힌트: 이렇게 이곳에 도착했습니다!):

`tldr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어</span>

- 특정 하위 명령에 대한 tldr 페이지를 출력:

`tldr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">하위_명령어</span>

- 주어진 [L]언어로 된 명령어의 tldr 페이지를 출력 (가능한 경우, 그렇지 않으면 영어로 표시):

`tldr --language `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">언어_코드</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어</span>

- 특정 [p]플랫폼의 명령어에 대한 tldr 페이지를 출력:

`tldr --platform `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">android|common|freebsd|linux|osx|netbsd|openbsd|sunos|windows</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어</span>

- tldr 페이지의 로컬 캐시 [u]업데이트:

`tldr --update`

- 현재 플랫폼 및 `common`에 대한 모든 페이지 [l]목록:

`tldr --list`

- 명령어에 대한 사용할 수 있는 모든 하위 명령 페이지 [l]목록:

`tldr --list | grep `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어</span>` | column`
