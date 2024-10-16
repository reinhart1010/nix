---
layout: page
title: common/exenv (한국어)
description: "Elixir 버전을 쉽게 설치하고 애플리케이션 환경을 관리."
content_hash: 4681fc961b56da8597f21e134b6a02f8f24d6b6f
last_modified_at: 2024-10-16
related_topics:
  - title: English version
    url: /en/common/exenv.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/exenv.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># exenv

Elixir 버전을 쉽게 설치하고 애플리케이션 환경을 관리.
더 많은 정보: <https://github.com/mururu/exenv>.

- 설치된 버전 목록 표시:

`exenv versions`

- 전체 시스템에서 특정 버전의 Elixir을 사용:

`exenv global `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">버전</span>

- 현재 애플리케이션/프로젝트 디렉토리에 특정 버전의 Elixir를 사용:

`exenv local `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">버전</span>

- Show the currently selected Elixir version:

`exenv `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">버전</span>

- Elixir 버전을 설치 (`elixir-build` <https://github.com/mururu/elixir-build> 플러그인 필요):

`exenv install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">버전</span>
