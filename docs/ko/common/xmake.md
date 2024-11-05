---
layout: page
title: common/xmake (한국어)
description: "Lua 기반의 크로스 플랫폼 C & C++ 빌드 유틸리티."
content_hash: fc75e082c37e78262efd9b54a0b8396e7d493add
last_modified_at: 2024-11-05
related_topics:
  - title: English version
    url: /en/common/xmake.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/xmake.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/xmake.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># xmake

Lua 기반의 크로스 플랫폼 C & C++ 빌드 유틸리티.
더 많은 정보: <https://xmake.io/#/getting_started>.

- Hello World와 `xmake.lua`를 포함한 Xmake C 프로젝트 생성:

`xmake create --language c -P `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">프로젝트_이름</span>

- Xmake 프로젝트 빌드 및 실행:

`xmake build run`

- 컴파일된 Xmake 타겟을 직접 실행:

`xmake run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">타겟_이름</span>

- 프로젝트의 빌드 타겟 구성:

`xmake config --plat=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">macosx|linux|iphoneos|...</span>` --arch=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">x86_64|i386|arm64|...</span>` --mode=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">debug|release</span>

- 컴파일된 타겟을 디렉토리에 설치:

`xmake install -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>
