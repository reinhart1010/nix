---
layout: page
title: common/dotnet-ef (한국어)
description: "Entity Framework Core용 디자인 타임 개발 작업 수행."
content_hash: e65743d9d15579ba8a86303be7e6e7d05011485d
last_modified_at: 2024-11-01
related_topics:
  - title: English version
    url: /en/common/dotnet-ef.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/dotnet-ef.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/dotnet-ef.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># dotnet ef

Entity Framework Core용 디자인 타임 개발 작업 수행.
더 많은 정보: <https://learn.microsoft.com/ef/core/cli/dotnet>.

- 지정된 마이그레이션으로 데이터베이스 업데이트:

`dotnet ef database update `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">마이그레이션</span>

- 데이터베이스 삭제:

`dotnet ef database drop`

- 사용 가능한 `DbContext` 유형 나열:

`dotnet ef dbcontext list`

- 데이터베이스에 대한 `DbContext` 및 엔티티 유형의 코드 생성:

`dotnet ef dbcontext scaffold `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">연결_문자열</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">프로바이더</span>

- 새 마이그레이션 추가:

`dotnet ef migrations add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름</span>

- 마지막 마이그레이션 제거 및 최신 마이그레이션에 대한 코드 변경 사항 롤백:

`dotnet ef migrations remove`

- 사용 가능한 마이그레이션 나열:

`dotnet ef migrations list`

- 마이그레이션 범위에서 SQL 스크립트 생성:

`dotnet ef migrations script `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">시작_마이그레이션</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">종료_마이그레이션</span>
