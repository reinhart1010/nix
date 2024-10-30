---
layout: page
title: linux/xsel (한국어)
description: "X11 선택 및 클립보드 조작 도구."
content_hash: 23dfd006c02ad30b5d31b43ee261c70553f3b7db
last_modified_at: 2024-10-30
related_topics:
  - title: English version
    url: /en/linux/xsel.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/xsel.html
    icon: bi bi-globe
tldri18n_status: 2
---
# xsel

X11 선택 및 클립보드 조작 도구.
더 많은 정보: <https://manned.org/xsel>.

- 명령의 출력을 클립보드 입력으로 사용 (Ctrl + C와 동일):

`echo 123 | xsel -ib`

- 파일의 내용을 클립보드 입력으로 사용:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>` | xsel -ib`

- 클립보드의 내용을 터미널에 출력 (Ctrl + V와 동일):

`xsel -ob`

- 클립보드의 내용을 파일에 출력:

`xsel -ob > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 클립보드 내용 지우기:

`xsel -cb`

- X11 기본 선택의 내용을 터미널에 출력 (마우스 중간 클릭과 동일):

`xsel -op`
