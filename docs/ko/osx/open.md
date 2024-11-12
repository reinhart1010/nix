---
layout: page
title: osx/open (한국어)
description: "파일, 디렉토리 및 애플리케이션을 엽니다."
content_hash: ccdb7daa20b276f67d0e8ca9be94fdab24acb250
last_modified_at: 2024-11-12
related_topics:
  - title: Deutsch version
    url: /de/osx/open.html
    icon: bi bi-globe
  - title: English version
    url: /en/osx/open.html
    icon: bi bi-globe
  - title: español version
    url: /es/osx/open.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/osx/open.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/osx/open.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/open.html
    icon: bi bi-globe
tldri18n_status: 2
---
# open

파일, 디렉토리 및 애플리케이션을 엽니다.
더 많은 정보: <https://keith.github.io/xcode-man-pages/open.1.html>.

- 파일을 관련 애플리케이션으로 열기:

`open `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일.ext</span>

- 그래픽 macOS [a]애플리케이션 실행:

`open -a "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">애플리케이션</span>`"`

- [b]번들 식별자를 기반으로 그래픽 macOS 앱 실행 (`osascript`를 사용하여 쉽게 얻을 수 있음):

`open -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">com.domain.application</span>

- 현재 디렉토리를 Finder에서 열기:

`open .`

- 파일을 Finder에서 [R]표시:

`open -R `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 현재 디렉토리에서 주어진 확장자의 모든 파일을 관련 애플리케이션으로 열기:

`open `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.확장자</span>

- [b]번들 식별자를 통해 지정된 애플리케이션의 [n]새 인스턴스 열기:

`open -n -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">com.domain.application</span>
