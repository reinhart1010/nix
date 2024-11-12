---
layout: page
title: linux/snap (한국어)
description: "\"snap\" 독립형 소프트웨어 패키지 관리."
content_hash: 38c38fc09474155c6ec78b15059c91f0a3b0936f
last_modified_at: 2024-11-12
related_topics:
  - title: বাংলা version
    url: /bn/linux/snap.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/snap.html
    icon: bi bi-globe
  - title: മലയാളം version
    url: /ml/linux/snap.html
    icon: bi bi-globe
tldri18n_status: 2
---
# snap

"snap" 독립형 소프트웨어 패키지 관리.
`.deb` 파일에 대한 `apt`와 유사.
더 많은 정보: <https://manned.org/snap>.

- 패키지 검색:

`snap find `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">검색어</span>

- 패키지 설치:

`snap install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>

- 패키지 업데이트:

`snap refresh `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>

- 패키지를 다른 채널(트랙, 위험도, 브랜치)로 업데이트:

`snap refresh `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>` --channel=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">채널</span>

- 모든 패키지 업데이트:

`snap refresh`

- 설치된 snap 소프트웨어의 기본 정보 표시:

`snap list`

- 패키지 제거:

`snap remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>

- 시스템의 최근 snap 변경 사항 확인:

`snap changes`
