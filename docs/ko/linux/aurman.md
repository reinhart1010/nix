---
layout: page
title: linux/aurman (한국어)
description: "Arch User Repository에서 패키지를 빌드하고 설치하는 Arch Linux 유틸리티."
content_hash: 0b2c1db4fc434e35b3f26c23eebf6e17ee001bea
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/aurman.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/aurman.html
    icon: bi bi-globe
tldri18n_status: 2
---
# aurman

Arch User Repository에서 패키지를 빌드하고 설치하는 Arch Linux 유틸리티.
같이 보기: `pacman`.
더 많은 정보: <https://github.com/polygamma/aurman>.

- 모든 패키지를 동기화하고 업데이트:

`aurman --sync --refresh --sysupgrade`

- `PKGBUILD` 파일의 변경 사항을 표시하지 않고 모든 패키지를 동기화하고 업데이트:

`aurman --sync --refresh --sysupgrade --noedit`

- 새 패키지 설치:

`aurman --sync `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>

- `PKGBUILD` 파일의 변경 사항을 표시하지 않고 새 패키지 설치:

`aurman --sync --noedit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>

- 묻지 않고 새 패키지 설치:

`aurman --sync --noedit --noconfirm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>

- 공식 저장소와 AUR에서 키워드를 검색하여 패키지 검색:

`aurman --sync --search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">키워드</span>

- 특정 패키지 및 의존성 제거:

`aurman --remove --recursive --nosave `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>

- 패키지 캐시 지우기 (모든 패키지를 삭제하려면 두 개의 `--clean` 플래그 사용):

`aurman --sync --clean`
