---
layout: page
title: windows/shutdown (한국어)
description: "컴퓨터를 종료, 재시작 또는 로그오프하는 도구입니다."
content_hash: ea9f7e5df96d6067a0a86663f219d4c985f4927f
last_modified_at: 2024-10-20
related_topics:
  - title: English version
    url: /en/windows/shutdown.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/windows/shutdown.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/shutdown.html
    icon: bi bi-globe
tldri18n_status: 2
---
# shutdown

컴퓨터를 종료, 재시작 또는 로그오프하는 도구입니다.
더 많은 정보: <https://learn.microsoft.com/windows-server/administration/windows-commands/shutdown>.

- 현재 컴퓨터 종료:

`shutdown /s`

- 현재 컴퓨터 강제 종료:

`shutdown /s /f`

- 현재 컴퓨터 즉시 재시작:

`shutdown /r /t 0`

- 현재 컴퓨터 최대 절전 모드:

`shutdown /h`

- 현재 컴퓨터 로그오프:

`shutdown /l`

- 종료 전 대기 시간 지정:

`shutdown /s /t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">8</span>

- 대기 시간이 만료되지 않은 종료 시퀀스 중단:

`shutdown /a`

- 원격 컴퓨터 종료:

`shutdown /m `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">\\호스트명</span>
