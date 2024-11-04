---
layout: page
title: windows/getmac (한국어)
description: "시스템의 MAC 주소를 표시."
content_hash: b452ca9f3754d53690778d033a31f9468dbf021e
last_modified_at: 2024-11-04
related_topics:
  - title: English version
    url: /en/windows/getmac.html
    icon: bi bi-globe
  - title: español version
    url: /es/windows/getmac.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/getmac.html
    icon: bi bi-globe
tldri18n_status: 2
---
# getmac

시스템의 MAC 주소를 표시.
더 많은 정보: <https://learn.microsoft.com/windows-server/administration/windows-commands/getmac>.

- 현재 시스템의 MAC 주소 표시:

`getmac`

- 특정 형식으로 세부 정보 표시:

`getmac /fo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">table|list|csv</span>

- 출력 목록에서 헤더 제외:

`getmac /nh`

- 원격 컴퓨터의 MAC 주소 표시:

`getmac /s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">호스트명</span>` /u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자명</span>` /p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">비밀번호</span>

- 자세한 정보와 함께 MAC 주소 표시:

`getmac /v`

- 도움말 표시:

`getmac /?`
