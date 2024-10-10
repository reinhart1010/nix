---
layout: page
title: windows/wmic (한국어)
description: "실행 중인 프로세스에 대한 세부 정보를 보는 데 사용되는 대화형 쉘입니다."
content_hash: 3df9a440078242392793325ee24d578ea7b5620d
last_modified_at: 2024-10-10
related_topics:
  - title: English version
    url: /en/windows/wmic.html
    icon: bi bi-globe
tldri18n_status: 2
---
# wmic

실행 중인 프로세스에 대한 세부 정보를 보는 데 사용되는 대화형 쉘입니다.
더 많은 정보: <https://learn.microsoft.com/windows-server/administration/windows-commands/wmic>.

- 기본 문법:

`wmic `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">별칭</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">where_구문</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">verb_구문</span>

- 현재 실행 중인 프로세스에 대한 간단한 세부 정보 표시:

`wmic process list brief`

- 현재 실행 중인 프로세스에 대한 전체 세부 정보 표시:

`wmic process list full`

- 프로세스 이름, 프로세스 ID 및 부모 프로세스 ID와 같은 특정 필드 접근:

`wmic process get `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름,프로세스_id,부모_프로세스_id</span>

- 특정 프로세스에 대한 정보 표시:

`wmic process where `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름="example.exe"</span>` list full`

- 특정 프로세스에 대한 특정 필드 표시:

`wmic process where processid=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">프로세스_id</span>` get `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름,명령어</span>

- 프로세스 종료:

`wmic process `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">프로세스_id</span>` delete`
