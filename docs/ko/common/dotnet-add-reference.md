---
layout: page
title: common/dotnet-add-reference (한국어)
description: ".NET 프로젝트 간 참조 추가."
content_hash: 013e7c94e729f6e3abdf46f2cacbc530f4557370
last_modified_at: 2024-11-01
related_topics:
  - title: English version
    url: /en/common/dotnet-add-reference.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/dotnet-add-reference.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># dotnet add reference

.NET 프로젝트 간 참조 추가.
더 많은 정보: <https://learn.microsoft.com/dotnet/core/tools/dotnet-add-reference>.

- 현재 디렉터리에 있는 프로젝트에 참조 추가:

`dotnet add reference `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/참조.csproj</span>

- 현재 디렉터리에 있는 프로젝트에 여러 참조 추가:

`dotnet add reference `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/참조1.csproj 경로/대상/참조2.csproj ...</span>

- 특정 프로젝트에 참조 추가:

`dotnet add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/프로젝트.csproj</span>` reference `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/참조.csproj</span>

- 특정 프로젝트에 여러 참조 추가:

`dotnet add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/프로젝트.csproj</span>` reference `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/참조1.csproj 경로/대상/참조2.csproj ...</span>
