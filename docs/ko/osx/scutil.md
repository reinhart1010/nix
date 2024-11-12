---
layout: page
title: osx/scutil (한국어)
description: "시스템 구성 매개변수를 관리합니다."
content_hash: 6dc17b5f8eacdd534a8462a3a1cdc2db99efd4ec
last_modified_at: 2024-11-12
related_topics:
  - title: English version
    url: /en/osx/scutil.html
    icon: bi bi-globe
  - title: español version
    url: /es/osx/scutil.html
    icon: bi bi-globe
  - title: português (Portugal) version
    url: /pt_PT/osx/scutil.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/scutil.html
    icon: bi bi-globe
tldri18n_status: 2
---
# scutil

시스템 구성 매개변수를 관리합니다.
구성 설정 시 루트 권한이 필요합니다.
더 많은 정보: <https://keith.github.io/xcode-man-pages/scutil.8.html>.

- DNS 구성 표시:

`scutil --dns`

- 프록시 구성 표시:

`scutil --proxy`

- 컴퓨터 이름 확인:

`scutil --get ComputerName`

- 컴퓨터 이름 설정:

`sudo scutil --set ComputerName `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">컴퓨터_이름</span>

- 호스트명 확인:

`scutil --get HostName`

- 호스트명 설정:

`scutil --set HostName `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">호스트명</span>
