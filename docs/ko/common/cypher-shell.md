---
layout: page
title: common/cypher-shell (한국어)
description: "대화형 세션을 열고 Neo4j 인스턴스에 대해 Cypher 쿼리를 실행."
content_hash: bd55e167046e64a9472c60f73beb35e9f956fd38
last_modified_at: 2024-10-11
related_topics:
  - title: English version
    url: /en/common/cypher-shell.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/cypher-shell.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/cypher-shell.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># cypher-shell

대화형 세션을 열고 Neo4j 인스턴스에 대해 Cypher 쿼리를 실행.
참고: `neo4j-admin`, `mysql`.
더 많은 정보: <https://neo4j.com/docs/operations-manual/current/tools/cypher-shell/>.

- 기본 포트에서 로컬 인스턴스에 연결 (`neo4j://localhost:7687`):

`cypher-shell`

- 원격 인스턴스에 연결:

`cypher-shell --address neo4j://`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">호스트</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">포트</span>

- 보안 자격 증명 연결 및 제공:

`cypher-shell --username `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자명</span>` --password `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">비밀번호</span>

- 특정 데이터베이스에 연결:

`cypher-shell --database `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">데이터베이스_이름</span>

- 파일에서 Cypher 문을 실행하고 닫음:

`cypher-shell --file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.cypher</span>

- 파일에 대한 로깅 활성화:

`cypher-shell --log `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.log</span>

- 도움말 표시:

`cypher-shell --help`
