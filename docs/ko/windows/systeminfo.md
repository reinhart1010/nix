---
layout: page
title: windows/systeminfo (한국어)
description: "로컬 또는 원격 컴퓨터의 운영 체제 구성 정보를 표시합니다."
content_hash: a8f573f04986df8d60eb3990faffda157d4f7fe1
last_modified_at: 2024-10-20
related_topics:
  - title: English version
    url: /en/windows/systeminfo.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/systeminfo.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/windows/systeminfo.html
    icon: bi bi-globe
tldri18n_status: 2
---
# systeminfo

로컬 또는 원격 컴퓨터의 운영 체제 구성 정보를 표시합니다.
더 많은 정보: <https://learn.microsoft.com/windows-server/administration/windows-commands/systeminfo>.

- 로컬 컴퓨터의 시스템 구성 표시:

`systeminfo`

- 지정된 출력 형식으로 시스템 구성 표시:

`systeminfo /fo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">표|목록|csv</span>

- 원격 컴퓨터의 시스템 구성 표시:

`systeminfo /s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">원격_이름</span>` /u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자명</span>` /p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">암호</span>

- 도움말 표시:

`systeminfo /?`
