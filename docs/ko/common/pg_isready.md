---
layout: page
title: common/pg_isready (한국어)
description: "PostgreSQL 서버의 연결 상태 확인."
content_hash: 2721294ba0599de01dadb567303810515777f2e4
last_modified_at: 2024-11-07
related_topics:
  - title: English version
    url: /en/common/pg_isready.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/pg_isready.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># pg_isready

PostgreSQL 서버의 연결 상태 확인.
더 많은 정보: <https://www.postgresql.org/docs/current/app-pg-isready.html>.

- 연결 상태 확인:

`pg_isready`

- 특정 호스트명과 포트를 사용하여 연결 상태 확인:

`pg_isready --host=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">호스트명</span>` --port=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">포트</span>

- 연결 실패 시에만 메시지 표시하며 연결 상태 확인:

`pg_isready --quiet`
