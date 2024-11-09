---
layout: page
title: common/snowsql (한국어)
description: "Snowflake의 데이터 클라우드를 위한 SnowSQL 커맨드라인 클라이언트."
content_hash: c4637b7aced045ed2d3b04856c1baffb7cf81111
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/common/snowsql.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/snowsql.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/snowsql.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># snowsql

Snowflake의 데이터 클라우드를 위한 SnowSQL 커맨드라인 클라이언트.
더 많은 정보: <https://docs.snowflake.com/en/user-guide/snowsql.html>.

- <https://account.snowflakecomputing.com>의 특정 인스턴스에 연결 (비밀번호는 프롬프트 또는 설정 파일에서 제공 가능):

`snowsql --accountname `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">계정</span>` --username `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자명</span>` --dbname `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">데이터베이스</span>` --schemaname `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">스키마</span>

- 특정 설정 파일에 지정된 인스턴스에 연결 (기본값은 `~/.snowsql/config`):

`snowsql --config `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/설정_파일</span>

- 다단계 인증 토큰을 사용하여 기본 인스턴스에 연결:

`snowsql --mfa-passcode `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">토큰</span>

- 기본 연결에서 단일 SQL 쿼리 또는 SnowSQL 명령 실행 (쉘 스크립트에서 유용):

`snowsql --query '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">쿼리</span>`'`

- 특정 파일에서 기본 연결로 명령 실행:

`snowsql --filename `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.sql</span>
