---
layout: page
title: osx/defaults (한국어)
description: "macOS 사용자 애플리케이션 구성을 읽고 쓰기."
content_hash: 427fb67f9002133511d0f0aa491a9790d5a44be7
last_modified_at: 2024-11-12
related_topics:
  - title: English version
    url: /en/osx/defaults.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/osx/defaults.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/defaults.html
    icon: bi bi-globe
tldri18n_status: 2
---
# defaults

macOS 사용자 애플리케이션 구성을 읽고 쓰기.
더 많은 정보: <https://keith.github.io/xcode-man-pages/defaults.1.html>.

- 애플리케이션 옵션에 대한 시스템 기본값 읽기:

`defaults read "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">애플리케이션</span>`" "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">옵션</span>`"`

- 애플리케이션 옵션에 대한 기본값 읽기:

`defaults read -app "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">애플리케이션</span>`" "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">옵션</span>`"`

- 도메인 이름, 키 및 값에서 키워드 검색:

`defaults find "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">키워드</span>`"`

- 애플리케이션 옵션의 기본값 쓰기:

`defaults write "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">애플리케이션</span>`" "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">옵션</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-타입</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">값</span>

- Mission Control 애니메이션 속도 향상:

`defaults write com.apple.Dock expose-animation-duration -float 0.1`

- 애플리케이션의 모든 기본값 삭제:

`defaults delete "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">애플리케이션</span>`"`
