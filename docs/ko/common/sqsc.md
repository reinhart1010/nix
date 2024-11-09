---
layout: page
title: common/sqsc (한국어)
description: "명령줄 AWS Simple Queue Service 클라이언트."
content_hash: 8c06c94ddaa1da6b0db15ba4c8065480922bde8a
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/common/sqsc.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/sqsc.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># sqsc

명령줄 AWS Simple Queue Service 클라이언트.
더 많은 정보: <https://github.com/yongfei25/sqsc>.

- 모든 큐 나열:

`sqsc lq `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">큐_접두사</span>

- 큐에 있는 모든 메시지 나열:

`sqsc ls `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">큐_이름</span>

- 한 큐의 모든 메시지를 다른 큐로 복사:

`sqsc cp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">소스_큐</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">대상_큐</span>

- 한 큐의 모든 메시지를 다른 큐로 이동:

`sqsc mv `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">소스_큐</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">대상_큐</span>

- 큐 설명:

`sqsc describe `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">큐_이름</span>

- SQL 구문을 사용하여 큐 조회:

`sqsc query "SELECT body FROM `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">큐_이름</span>` WHERE body LIKE '%user%'"`

- 현재 작업 디렉토리의 로컬 SQLite 데이터베이스로 큐의 모든 메시지 가져오기:

`sqsc pull `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">큐_이름</span>
