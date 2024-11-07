---
layout: page
title: common/monop (한국어)
description: ".NET 어셈블리 내의 타입 및 메서드 시그니처를 찾아 표시."
content_hash: a59075cccba4e940ebb34cf6bf937624bc4fee8f
last_modified_at: 2024-11-07
related_topics:
  - title: English version
    url: /en/common/monop.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/monop.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># monop

.NET 어셈블리 내의 타입 및 메서드 시그니처를 찾아 표시.
더 많은 정보: <https://manned.org/monop>.

- .NET Framework의 내장 타입 구조 표시:

`monop `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">System.String</span>

- 어셈블리 내 타입 나열:

`monop -r:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/어셈블리.exe</span>

- 특정 어셈블리의 타입 구조 표시:

`monop -r:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/어셈블리.dll</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">네임스페이스.경로.대상.타입</span>

- 지정된 타입에 정의된 멤버만 표시:

`monop -r:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/어셈블리.dll</span>` --only-declared `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">네임스페이스.경로.대상.타입</span>

- 비공개 멤버 표시:

`monop -r:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/어셈블리.dll</span>` --private `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">네임스페이스.경로.대상.타입</span>

- 사용되지 않는 멤버 숨기기:

`monop -r:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/어셈블리.dll</span>` --filter-obsolete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">네임스페이스.경로.대상.타입</span>

- 특정 어셈블리가 참조하는 다른 어셈블리 나열:

`monop -r:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/어셈브리.dll</span>` --refs`
