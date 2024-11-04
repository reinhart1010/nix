---
layout: page
title: windows/iscc (한국어)
description: "Inno Setup 설치 프로그램용 컴파일러입니다."
content_hash: 9126abce9b0268d0025864fb3f45d9178c527e20
last_modified_at: 2024-11-04
related_topics:
  - title: English version
    url: /en/windows/iscc.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/iscc.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/windows/iscc.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># iscc

Inno Setup 설치 프로그램용 컴파일러입니다.
이는 Inno Setup 스크립트를 Windows 설치 프로그램 실행 파일로 컴파일합니다.
더 많은 정보: <https://jrsoftware.org/isinfo.php>.

- Inno Setup 스크립트를 컴파일:

`iscc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로\대상\파일.iss</span>

- Inno Setup 설치 프로그램을 조용히 컴파일:

`iscc /Q `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로\대상\파일.iss</span>

- 서명된 Inno Setup 설치 프로그램 컴파일:

`iscc /S=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로\대상\파일.iss</span>
