---
layout: page
title: common/conan (한국어)
description: "모든 기본 바이너리를 생성하고 공유할 수 있는 오픈소스, 분산형 및 크로스 플랫폼 패키지 관리자."
content_hash: 203ea2966bc2d7688ce895be8dd13d55adc1cc26
last_modified_at: 2024-10-11
related_topics:
  - title: English version
    url: /en/common/conan.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/conan.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># conan

모든 기본 바이너리를 생성하고 공유할 수 있는 오픈소스, 분산형 및 크로스 플랫폼 패키지 관리자.
`frogarian`과 같은 일부 하위 명령에는 자체 사용법 문서가 있음.
더 많은 정보: <https://conan.io/>.

- `conanfile.txt`를 기반으로 패키지를 설치:

`conan install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">.</span>

- 패키지를 설치하고 특정 생성기에 대한 구성 파일을 만듬:

`conan install -g `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">생성기</span>

- 소스에서 빌드하여 패키지를 설치:

`conan install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">.</span>` --build`

- 로컬에 설치된 패키지 검색:

`conan search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>

- 원격 패키지 검색:

`conan search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>` -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">원격</span>

- 원격 패키지 목록:

`conan remote list`
