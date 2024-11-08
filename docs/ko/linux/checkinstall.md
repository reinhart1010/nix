---
layout: page
title: linux/checkinstall (한국어)
description: "소프트웨어 패키지의 로컬 설치를 추적하고 시스템의 기본 패키지 관리 도구와 함께 사용할 수 있는 바이너리 패키지를 생성합니다."
content_hash: f418b2b7bb5dcaf2c52389a1fa5e9c2293b4226b
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/linux/checkinstall.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/checkinstall.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># checkinstall

소프트웨어 패키지의 로컬 설치를 추적하고 시스템의 기본 패키지 관리 도구와 함께 사용할 수 있는 바이너리 패키지를 생성합니다.
더 많은 정보: <https://checkinstall.izto.org>.

- 기본 설정으로 패키지를 생성하고 설치:

`sudo checkinstall --default`

- 패키지를 생성하지만 설치하지 않음:

`sudo checkinstall --install=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">no</span>

- 문서 없이 패키지 생성:

`sudo checkinstall --nodoc`

- 패키지를 생성하고 이름 설정:

`sudo checkinstall --pkgname `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>

- 패키지를 생성하고 저장할 위치 지정:

`sudo checkinstall --pakdir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>
