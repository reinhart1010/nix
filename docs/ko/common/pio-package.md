---
layout: page
title: common/pio-package (한국어)
description: "레지스트리에서 패키지를 관리."
content_hash: 9c103f500a26b05110f9d54127bee553a3f10497
last_modified_at: 2024-11-02
related_topics:
  - title: English version
    url: /en/common/pio-package.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/pio-package.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/pio-package.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># pio package

레지스트리에서 패키지를 관리.
패키지는 게시된 날짜로부터 72시간(3일) 이내에만 제거할 수 있습니다.
더 많은 정보: <https://docs.platformio.org/en/latest/core/userguide/package/>.

- 현재 디렉토리에서 패키지 tarball 생성:

`pio package pack --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/package.tar.gz</span>

- 현재 디렉토리에서 패키지 tarball 생성 및 게시:

`pio package publish`

- 현재 디렉토리를 게시하고 공개 접근 제한:

`pio package publish --private`

- 패키지 게시:

`pio package publish `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/package.tar.gz</span>

- 사용자 지정 릴리스 날짜(UTC)로 패키지 게시:

`pio package publish `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/package.tar.gz</span>` --released-at "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2021-04-08 21:15:38</span>`"`

- 게시된 패키지의 모든 버전을 레지스트리에서 제거:

`pio package unpublish `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>

- 게시된 패키지의 특정 버전을 레지스트리에서 제거:

`pio package unpublish `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">버전</span>

- 제거를 취소하고 패키지의 모든 버전 또는 특정 버전을 레지스트리에 복원:

`pio package unpublish --undo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">버전</span>
