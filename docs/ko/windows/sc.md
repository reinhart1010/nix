---
layout: page
title: windows/sc (한국어)
description: "Service Control Manager 및 서비스와 통신합니다."
content_hash: d92ba456ef080d4cd85c1d2b047075d792f79185
last_modified_at: 2024-10-25
related_topics:
  - title: English version
    url: /en/windows/sc.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/windows/sc.html
    icon: bi bi-globe
tldri18n_status: 2
---
# sc

Service Control Manager 및 서비스와 통신합니다.
더 많은 정보: <https://learn.microsoft.com/windows-server/administration/windows-commands/sc-query>.

- 서비스 상태 표시 (서비스 이름이 없으면 모든 서비스 표시):

`sc.exe query `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">서비스명</span>

- 서비스 비동기적으로 시작:

`sc.exe create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">서비스명</span>` binpath= `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로\대상\서비스_이진_파일</span>

- 서비스 비동기적으로 중지:

`sc.exe delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">서비스명</span>

- 서비스 유형 설정:

`sc.exe config `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">서비스명</span>` type= `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">서비스_유형</span>
