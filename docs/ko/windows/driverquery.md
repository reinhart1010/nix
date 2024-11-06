---
layout: page
title: windows/driverquery (한국어)
description: "설치된 장치 드라이버에 대한 정보를 표시."
content_hash: 84429671689f743c90c0a8ebb3961c41ce3d0b66
last_modified_at: 2024-11-06
related_topics:
  - title: English version
    url: /en/windows/driverquery.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/driverquery.html
    icon: bi bi-globe
tldri18n_status: 2
---
# driverquery

설치된 장치 드라이버에 대한 정보를 표시.
더 많은 정보: <https://learn.microsoft.com/windows-server/administration/windows-commands/driverquery>.

- 설치된 모든 장치 드라이버 목록 표시:

`driverquery`

- 지정된 형식으로 드라이버 목록 표시:

`driverquery /fo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">table|list|csv</span>

- 서명 여부를 나타내는 열과 함께 드라이버 목록 표시:

`driverquery /si`

- 출력 목록에서 헤더 제외:

`driverquery /nh`

- 원격 컴퓨터의 드라이버 목록 표시:

`driverquery /s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">호스트명</span>` /u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자명</span>` /p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">비밀번호</span>

- 자세한 정보와 함께 드라이버 목록 표시:

`driverquery /v`

- 도움말 표시:

`driverquery /?`
