---
layout: page
title: windows/vswhere (한국어)
description: "Visual Studio 2017 및 더 최신 설치를 찾습니다."
content_hash: 4a45da4b504331ef0167b936bda3f3723d561d7b
last_modified_at: 2024-10-11
related_topics:
  - title: English version
    url: /en/windows/vswhere.html
    icon: bi bi-globe
tldri18n_status: 2
---
# vswhere

Visual Studio 2017 및 더 최신 설치를 찾습니다.
더 많은 정보: <https://github.com/microsoft/vswhere>.

- vcvarsall.bat의 경로를 찾아 환경 변수를 설정:

`vswhere -products * -latest -prerelease -find **\VC\Auxiliary\Build\vcvarsall.bat`

- x64 MSVC 컴파일러 (cl.exe 등)의 디렉토리 찾기:

`vswhere -products * -latest -prerelease -find **\Hostx64\x64\*`

- Visual Studio에 포함된 Clang (clang-cl, clang-tidy 등)의 디렉토리 찾기:

`vswhere -products * -latest -prerelease -find **\Llvm\bin\*`

- `MSBuild.exe`의 경로 찾기:

`vswhere -products * -latest -prerelease -find MSBuild\**\Bin\MSBuild.exe`
