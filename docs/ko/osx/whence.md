---
layout: page
title: osx/whence (한국어)
description: "Zsh 내장 명령어로, 명령어가 어떻게 해석될지를 나타냅니다."
content_hash: 1d86288674db525123d4bc2c6992ee470d0c4cec
last_modified_at: 2024-11-12
related_topics:
  - title: English version
    url: /en/osx/whence.html
    icon: bi bi-globe
  - title: español version
    url: /es/osx/whence.html
    icon: bi bi-globe
tldri18n_status: 2
---
# whence

Zsh 내장 명령어로, 명령어가 어떻게 해석될지를 나타냅니다.
더 많은 정보: <https://keith.github.io/xcode-man-pages/whence.1.html>.

- `command`를 해석하고, `alias`로 정의된 경우 확장:

`whence "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어</span>`"`

- `command`의 유형을 표시하고, 함수나 바이너리로 정의된 경우 위치도 함께 표시:

`whence -v "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어</span>`"`

- 위와 동일하지만, 위치 대신 셸 함수의 내용을 표시:

`whence -c "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어</span>`"`

- 위와 동일하지만, 명령어 경로상의 모든 발생을 표시:

`whence -ca "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어</span>`"`

- `PATH`에서만 `command`를 검색하고, 내장 명령어, 별칭 또는 셸 함수를 무시:

`whence -p "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어</span>`"`
