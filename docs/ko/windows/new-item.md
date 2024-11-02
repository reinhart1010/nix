---
layout: page
title: windows/new-item (한국어)
description: "새 파일, 디렉토리, 심볼릭 링크 또는 레지스트리 항목을 만듭니다."
content_hash: 388c7a8e5a9dd513ee45ec081ed3b707c9106b89
last_modified_at: 2024-11-02
related_topics:
  - title: English version
    url: /en/windows/new-item.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/windows/new-item.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/windows/new-item.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># New-Item

새 파일, 디렉토리, 심볼릭 링크 또는 레지스트리 항목을 만듭니다.
참고: 이 명령은 PowerShell을 통해서만 사용할 수 있습니다.
더 많은 정보: <https://learn.microsoft.com/powershell/module/microsoft.powershell.management/new-item>.

- 새 빈 파일 만들기 ( `touch`와 동일):

`New-Item `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로\대상\파일</span>

- 새 디렉토리 만들기:

`New-Item -ItemType Directory `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로\대상\디렉토리</span>

- 지정된 내용으로 새 텍스트 파일 만들기:

`New-Item `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로\대상\파일</span>` -Value `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">내용</span>

- 동일한 텍스트 파일을 여러 위치에 쓰기:

`New-Item `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로\대상\파일1 , 경로\대상\파일2 , ...</span>` -Value `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">내용</span>

- 파일 또는 디렉토리에 심볼릭 링크\하드 링크\교차점 만들기:

`New-Item -ItemType `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">SymbolicLink|HardLink|Junction</span>` -Path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로\대상\링크_파일</span>` -Target `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로\대상\소스_파일_또는_디렉토리</span>

- 새 빈 레지스트리 항목 만들기 (REG_SZ 사용 시 `New-ItemProperty` 또는 `Set-ItemProperty` 사용):

`New-Item `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로\대상\레지스트리_키</span>

- 지정된 값으로 새 빈 레지스트리 항목 만들기:

`New-Item `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로\대상\레지스트리_키</span>` -Value `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">값</span>
