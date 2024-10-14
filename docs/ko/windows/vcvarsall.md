---
layout: page
title: windows/vcvarsall (한국어)
description: "Microsoft Visual Studio 도구를 사용하기 위해 필요한 환경 변수를 설정합니다."
content_hash: 0a6da462b0a26fa96ceb70b5f2108a89a79ae530
last_modified_at: 2024-10-14
related_topics:
  - title: English version
    url: /en/windows/vcvarsall.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/windows/vcvarsall.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># vcvarsall

Microsoft Visual Studio 도구를 사용하기 위해 필요한 환경 변수를 설정합니다.
특정 Visual Studio 설치에 대한 `vcvarsall` 경로는 `vswhere`를 사용하여 찾을 수 있습니다.
더 많은 정보: <https://learn.microsoft.com/cpp/build/building-on-the-command-line>.

- 네이티브 x64 환경 설정:

`vcvarsall x64`

- x64 호스트에서 네이티브 x86 크로스 컴파일 환경 설정:

`vcvarsall x64_x86`

- x64 호스트에서 네이티브 Arm x64 크로스 컴파일 환경 설정:

`vcvarsall x64_arm64`

- 네이티브 UWP x64 환경 설정:

`vcvarsall x64 uwp`
