---
layout: page
title: windows/tasklist (한국어)
description: "로컬 또는 원격 머신에서 현재 실행 중인 프로세스 목록을 표시합니다."
content_hash: 6cbb2af732329aa0fca498907f708bda76f77d14
last_modified_at: 2024-10-17
related_topics:
  - title: English version
    url: /en/windows/tasklist.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/windows/tasklist.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/tasklist.html
    icon: bi bi-globe
tldri18n_status: 2
---
# tasklist

로컬 또는 원격 머신에서 현재 실행 중인 프로세스 목록을 표시합니다.
더 많은 정보: <https://learn.microsoft.com/windows-server/administration/windows-commands/tasklist>.

- 현재 실행 중인 프로세스 표시:

`tasklist`

- 지정된 출력 형식으로 실행 중인 프로세스 표시:

`tasklist /fo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">표|목록|csv</span>

- 지정된 `.exe` 또는 `.dll` 파일 이름으로 실행 중인 프로세스 표시:

`tasklist /m `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">모듈_패턴</span>

- 원격 머신에서 실행 중인 프로세스 표시:

`tasklist /s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">원격_이름</span>` /u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자명</span>` /p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">암호</span>

- 각 프로세스에서 사용하는 서비스 표시:

`tasklist /svc`
