---
layout: page
title: windows/move-item (한국어)
description: "파일, 디렉토리, 레지스트리 키 및 기타 PowerShell 데이터 항목을 이동 또는 이름을 변경합니다."
content_hash: 4c5304ea5c941c6e470bd0e1f4a1fc58b49b05fd
last_modified_at: 2024-11-02
related_topics:
  - title: English version
    url: /en/windows/move-item.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/windows/move-item.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/windows/move-item.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># Move-Item

파일, 디렉토리, 레지스트리 키 및 기타 PowerShell 데이터 항목을 이동 또는 이름을 변경합니다.
이 명령어는 PowerShell을 통해서만 실행할 수 있습니다.
더 많은 정보: <https://learn.microsoft.com/powershell/module/microsoft.powershell.management/move-item>.

- 목표가 기존 디렉토리가 아닐 때 파일 또는 디렉토리 이름 변경:

`Move-Item `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로\대상\소스</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로\대상\목표</span>

- 파일 또는 디렉토리를 기존 디렉토리로 이동:

`Move-Item `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로\대상\소스</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로\대상\기존_디렉토리</span>

- 특정 이름을 가진 파일 또는 디렉토리 이름 변경 또는 이동 (문자열 내 특수 문자 처리 안함):

`Move-Item -LiteralPath "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로\대상\소스</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로\대상\파일_또는_디렉토리</span>

- 여러 파일을 기존 디렉토리로 이동하고 파일 이름 변경 안함:

`Move-Item `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로\대상\소스1 , 경로\대상\소스2 ...</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로\대상\기존_디렉토리</span>

- 레지스트리 키 이동 또는 이름 변경:

`Move-Item `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로\대상\소스_키1 , 경로\대상\소스_키2 ...</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로\대상\새로운_또는_기존_키</span>

- 기존 파일 또는 레지스트리 키 덮어쓰기 전에 확인 안함:

`mv -Force `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로\대상\소스</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로\대상\목표</span>

- 파일 권한에 관계없이 기존 파일을 덮어쓰기 전에 확인 메시지를 표시:

`mv -Confirm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로\대상\소스</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로\대상\목표</span>

- 건너뛰기 모드로 파일 이동, 이동할 파일 및 디렉토리 표시:

`mv -WhatIf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로\대상\소스</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로\대상\목표</span>
