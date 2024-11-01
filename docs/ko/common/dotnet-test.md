---
layout: page
title: common/dotnet-test (한국어)
description: ".NET 애플리케이션의 테스트를 실행."
content_hash: ca8d5929ccd8816c701f5ae1a91ee09c7313daf2
last_modified_at: 2024-11-01
related_topics:
  - title: English version
    url: /en/common/dotnet-test.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/dotnet-test.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># dotnet test

.NET 애플리케이션의 테스트를 실행.
참고: 지원되는 필터 표현식은 <https://learn.microsoft.com/en-us/dotnet/core/testing/selective-unit-tests>를 참조.
더 많은 정보: <https://learn.microsoft.com/dotnet/core/tools/dotnet-test>.

- 현재 디렉토리의 .NET 프로젝트/솔루션에 대한 테스트 실행:

`dotnet test`

- 특정 위치에 있는 .NET 프로젝트/솔루션에 대한 테스트 실행:

`dotnet test `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/프로젝트_또는_솔루션</span>

- 주어진 필터 표현식과 일치하는 테스트 실행:

`dotnet test --filter `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Name~TestMethod1</span>
