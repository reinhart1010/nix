---
layout: page
title: linux/auracle (한국어)
description: "Arch Linux의 사용자 저장소(AUR)와 상호작용하기 위한 명령줄 도구."
content_hash: 0cc9c78061537935d26b2e7993273810f95bf7c5
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/linux/auracle.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/auracle.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/auracle.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># auracle

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
