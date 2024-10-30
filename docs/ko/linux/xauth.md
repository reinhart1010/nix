---
layout: page
title: linux/xauth (한국어)
description: "X 서버에 연결할 때 사용되는 인증 정보를 편집하고 표시."
content_hash: 495fe6f787da22ffba87629ec7bf3bc7319c16e3
last_modified_at: 2024-10-30
related_topics:
  - title: English version
    url: /en/linux/xauth.html
    icon: bi bi-globe
tldri18n_status: 2
---
# xauth

X 서버에 연결할 때 사용되는 인증 정보를 편집하고 표시.
더 많은 정보: <https://manned.org/xauth>.

- 특정 인증 파일로 대화형 모드 시작 (`~/.Xauthority`가 기본값):

`xauth -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 인증 파일에 대한 정보 표시:

`xauth info`

- 모든 디스플레이에 대한 인증 항목 표시:

`xauth list`

- 특정 디스플레이에 대한 인증 추가:

`xauth add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">디스플레이_이름</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">프로토콜_이름</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">키</span>

- 특정 디스플레이에 대한 인증 제거:

`xauth remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">디스플레이_이름</span>

- 현재 디스플레이에 대한 인증 항목을 `stdout`에 출력:

`xauth extract - $DISPLAY`

- 특정 파일에서 인증 항목을 인증 데이터베이스에 병합:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>` | xauth merge -`

- 도움말 표시:

`xauth --help`
