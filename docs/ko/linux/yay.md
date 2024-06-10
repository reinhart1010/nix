---
layout: page
title: linux/yay (한국어)
description: "Yet Another Yogurt: Arch User Repository(AUR)에서 패키지를 빌드하고 설치합니다."
content_hash: a637c5405589a25bd58b926f1dee978a02cc5544
last_modified_at: 2024-06-10
related_topics:
  - title: Deutsch version
    url: /de/linux/yay.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/yay.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/yay.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/yay.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/yay.html
    icon: bi bi-globe
tldri18n_status: 2
---
# yay

Yet Another Yogurt: Arch User Repository(AUR)에서 패키지를 빌드하고 설치합니다.
같이 보기: `pacman`.
더 많은 정보: <https://github.com/Jguer/yay>.

- 저장소와 AUR에서 패키지를 검색하고 상호작용하며 설치:

`yay `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지_이름|검색어</span>

- 저장소와 AUR의 모든 패키지를 동기화하고 업데이트:

`yay`

- AUR 패키지만 동기화하고 업데이트:

`yay -Sua`

- 저장소와 AUR에서 새 패키지 설치:

`yay -S `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>

- 설치된 패키지와 그 의존성 및 구성 파일 제거:

`yay -Rns `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>

- 저장소와 AUR의 패키지 데이터베이스에서 키워드 검색:

`yay -Ss `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">키워드</span>

- 고아 패키지 제거 (의존성으로 설치되었지만 더 이상 어떤 패키지도 필요로 하지 않는 패키지):

`yay -Yc`

- 설치된 패키지와 시스템 상태에 대한 통계 표시:

`yay -Ps`
