---
layout: page
title: osx/lipo (한국어)
description: "Mach-O 유니버설 바이너리를 처리합니다."
content_hash: 07794dd8c567a62aac9a79c32c6b6a8698ca9e4f
last_modified_at: 2024-11-12
related_topics:
  - title: English version
    url: /en/osx/lipo.html
    icon: bi bi-globe
  - title: español version
    url: /es/osx/lipo.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/osx/lipo.html
    icon: bi bi-globe
tldri18n_status: 2
---
# lipo

Mach-O 유니버설 바이너리를 처리합니다.
더 많은 정보: <https://keith.github.io/xcode-man-pages/lipo.1.html>.

- 두 개의 단일 아키텍처 파일에서 유니버설 파일 생성:

`lipo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/바이너리_파일.x86_64</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/바이너리_파일.arm64e</span>` -create -output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/바이너리_파일</span>

- 유니버설 파일에 포함된 모든 아키텍처 나열:

`lipo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/바이너리_파일</span>` -archs`

- 유니버설 파일에 대한 자세한 정보 표시:

`lipo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/바이너리_파일</span>` -detailed_info`

- 유니버설 파일에서 단일 아키텍처 파일 추출:

`lipo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/바이너리_파일</span>` -thin `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arm64e</span>` -output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/바이너리_파일.arm64e</span>
