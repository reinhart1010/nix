---
layout: page
title: common/vcpkg (한국어)
description: "C/C++ 라이브러리를 위한 패키지 관리자."
content_hash: b67e492c18879ddee05b986cc5f352b780292298
last_modified_at: 2024-11-04
related_topics:
  - title: English version
    url: /en/common/vcpkg.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/vcpkg.html
    icon: bi bi-globe
tldri18n_status: 2
---
# vcpkg

C/C++ 라이브러리를 위한 패키지 관리자.
참고: 패키지는 시스템에 설치되지 않습니다. 사용하려면 빌드 시스템(예: CMake)에 `vcpkg`를 사용하도록 지정해야 합니다.
더 많은 정보: <https://learn.microsoft.com/en-us/vcpkg/>.

- `vcpkg` 환경에 `libcurl` 패키지를 빌드하고 추가:

`vcpkg install curl`

- `emscripten` 도구 체인을 사용하여 `zlib`를 빌드하고 추가:

`vcpkg install --triplet=wasm32-emscripten zlib`

- 패키지 검색:

`vcpkg search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지_이름</span>

- CMake 프로젝트를 `vcpkg` 패키지를 사용하도록 설정:

`cmake -B build -DCMAKE_TOOLCHAIN_FILE=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/vcpkg_설치_디렉토리</span>`/scripts/buildsystems/vcpkg.cmake`
