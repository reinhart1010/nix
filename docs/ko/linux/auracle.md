---
layout: page
title: linux/auracle (한국어)
description: "Arch Linux의 사용자 저장소(AUR)와 상호작용하기 위한 명령줄 도구."
content_hash: 0cc9c78061537935d26b2e7993273810f95bf7c5
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/auracle.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/auracle.html
    icon: bi bi-globe
tldri18n_status: 2
---
# auracle

Arch Linux의 사용자 저장소(AUR)와 상호작용하기 위한 명령줄 도구.
더 많은 정보: <https://github.com/falconindy/auracle>.

- 정규 표현식과 일치하는 AUR 패키지 표시:

`auracle search '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">정규_표현식</span>`'`

- 하나 이상의 AUR 패키지에 대한 정보 표시:

`auracle info `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지1 패키지2 ...</span>

- 하나 이상의 AUR 패키지에 대한 `PKGBUILD` 파일(빌드 정보) 표시:

`auracle show `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지1 패키지2 ...</span>

- 설치된 AUR 패키지의 업데이트 표시:

`auracle outdated`
