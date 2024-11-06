---
layout: page
title: windows/diskpart (한국어)
description: "디스크, 볼륨 및 파티션 관리 도구."
content_hash: f8f17fa3beeb12648297a558a78a9851b97e724e
last_modified_at: 2024-11-06
related_topics:
  - title: English version
    url: /en/windows/diskpart.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/windows/diskpart.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/windows/diskpart.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/windows/diskpart.html
    icon: bi bi-globe
tldri18n_status: 2
---
# diskpart

디스크, 볼륨 및 파티션 관리 도구.
더 많은 정보: <https://learn.microsoft.com/windows-server/administration/windows-commands/diskpart>.

- 관리 명령 프롬프트에서 diskpart를 실행하여 명령줄에 진입:

`diskpart`

- 모든 디스크 나열:

`list disk`

- 볼륨 선택:

`select volume `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">볼륨</span>

- 선택된 볼륨에 드라이브 문자 할당:

`assign letter `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">문자</span>

- 새 파티션 생성:

`create partition primary`

- 선택된 볼륨 활성화:

`active`

- diskpart 종료:

`exit`
