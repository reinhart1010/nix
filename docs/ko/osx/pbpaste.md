---
layout: page
title: osx/pbpaste (한국어)
description: "클립보드의 내용을 `stdout`으로 전송."
content_hash: d0d783e64a20d7c8ffc5bedc4ee9a374a6d37dd1
last_modified_at: 2024-11-12
related_topics:
  - title: Deutsch version
    url: /de/osx/pbpaste.html
    icon: bi bi-globe
  - title: English version
    url: /en/osx/pbpaste.html
    icon: bi bi-globe
  - title: español version
    url: /es/osx/pbpaste.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/osx/pbpaste.html
    icon: bi bi-globe
  - title: ไทย version
    url: /th/osx/pbpaste.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/pbpaste.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pbpaste

클립보드의 내용을 `stdout`으로 전송.
키보드에서 Cmd + V를 누르는 것과 유사.
더 많은 정보: <https://keith.github.io/xcode-man-pages/pbpaste.1.html>.

- 클립보드의 내용을 [f]파일에 쓰기:

`pbpaste > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 클립보드의 내용을 명령어의 입력으로 사용:

`pbpaste | grep foo`
