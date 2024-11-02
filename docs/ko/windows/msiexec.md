---
layout: page
title: windows/msiexec (한국어)
description: "MSI 및 MSP 패키지 파일을 사용하여 Windows 프로그램 설치, 업데이트, 수리 또는 제거."
content_hash: 73c656e7c867a7fe6afbd89b5152dff948bdfc26
last_modified_at: 2024-11-02
related_topics:
  - title: English version
    url: /en/windows/msiexec.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/windows/msiexec.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/windows/msiexec.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/windows/msiexec.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># msiexec

MSI 및 MSP 패키지 파일을 사용하여 Windows 프로그램 설치, 업데이트, 수리 또는 제거.
더 많은 정보: <https://learn.microsoft.com/windows-server/administration/windows-commands/msiexec>.

- MSI 패키지에서 프로그램 설치:

`msiexec /package `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로\대상\파일.msi</span>

- 웹사이트에서 MSI 패키지 설치:

`msiexec /package `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com/installer.msi</span>

- MSP 패치 파일 설치:

`msiexec /update `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로\대상\파일.msp</span>

- 프로그램 또는 패치 제거 (각각의 MSI 또는 MSP 파일 사용):

`msiexec /uninstall `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로\대상\파일</span>
