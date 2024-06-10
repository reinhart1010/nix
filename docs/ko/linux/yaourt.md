---
layout: page
title: linux/yaourt (한국어)
description: "Arch Linux 유틸리티로 Arch User Repository(AUR)에서 패키지를 빌드합니다."
content_hash: b671b131b585284a3d215873a40f2486ab9415f0
last_modified_at: 2024-06-10
related_topics:
  - title: English version
    url: /en/linux/yaourt.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/yaourt.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/yaourt.html
    icon: bi bi-globe
tldri18n_status: 2
---
# yaourt

Arch Linux 유틸리티로 Arch User Repository(AUR)에서 패키지를 빌드합니다.
더 많은 정보: <https://linuxcommandlibrary.com/man/yaourt>.

- 모든 패키지 동기화 및 업데이트 (AUR 포함):

`yaourt -Syua`

- 새 패키지 설치 (AUR 포함):

`yaourt -S `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>

- 패키지와 그 의존성 제거 (AUR 패키지 포함):

`yaourt -Rs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>

- 키워드로 패키지 데이터베이스 검색 (AUR 포함):

`yaourt -Ss `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">검색어</span>

- 설치된 패키지, 버전 및 저장소 나열 (AUR 패키지는 'local' 저장소로 나열됨):

`yaourt -Q`
