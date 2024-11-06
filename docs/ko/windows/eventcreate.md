---
layout: page
title: windows/eventcreate (한국어)
description: "이벤트 로그에 사용자 정의 항목을 생성."
content_hash: 74c08a37964bbd488e3cc509697588677da6056f
last_modified_at: 2024-11-06
related_topics:
  - title: English version
    url: /en/windows/eventcreate.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/windows/eventcreate.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/eventcreate.html
    icon: bi bi-globe
tldri18n_status: 2
---
# eventcreate

이벤트 로그에 사용자 정의 항목을 생성.
이벤트 ID는 1에서 1000 사이의 숫자여야 함.
더 많은 정보: <https://learn.microsoft.com/windows-server/administration/windows-commands/eventcreate>.

- 로그에 주어진 ID(1-1000)로 새로운 이벤트 생성:

`eventcreate /t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">성공|오류|경고|정보</span>` /id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id</span>` /d "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">메시지</span>`"`

- 특정 이벤트 로그에 이벤트 생성:

`eventcreate /l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">로그_이름</span>` /t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">유형</span>` /id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id</span>` /d "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">메시지</span>`"`

- 특정 소스로 이벤트 생성:

`eventcreate /so `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">소스_이름</span>` /t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">유형</span>` /id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id</span>` /d "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">메시지</span>`"`

- 원격 컴퓨터의 이벤트 로그에 이벤트 생성:

`eventcreate /s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">호스트명</span>` /u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자명</span>` /p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">비밀번호</span>` /t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">유형</span>` /id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id</span>` /d "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">메시지</span>`"`
