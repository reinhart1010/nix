---
layout: page
title: windows/choco-pack (한국어)
description: "NuGet 사양을 `nupkg` 파일로 패키징."
content_hash: 8b1a03d461f8ffdcbbdb7e3fec32318540fb3e8b
last_modified_at: 2024-10-15
related_topics:
  - title: Deutsch version
    url: /de/windows/choco-pack.html
    icon: bi bi-globe
  - title: English version
    url: /en/windows/choco-pack.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/windows/choco-pack.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/windows/choco-pack.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/choco-pack.html
    icon: bi bi-globe
tldri18n_status: 2
---
# choco pack

NuGet 사양을 `nupkg` 파일로 패키징.
더 많은 정보: <https://chocolatey.org/docs/commands-pack>.

- NuGet 사양을 `nupkg` 파일로 패키징:

`choco pack `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로\대상\사양_파일</span>

- 결과 파일의 버전을 지정하여 NuGet 사양 패키징:

`choco pack `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로\대상\사양_파일</span>` --version `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">버전</span>

- 특정 디렉토리에 NuGet 사양 패키징:

`choco pack `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로\대상\사양_파일</span>` --output-directory `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로\대상\출력_디렉토리</span>
