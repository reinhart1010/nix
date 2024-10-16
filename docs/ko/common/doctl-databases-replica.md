---
layout: page
title: common/doctl-databases-replica (한국어)
description: "데이터베이스 클러스터와 연결된 읽기 전용 복제본을 관리."
content_hash: 91ef364964af5821d1484ab5376fa40a657ec88e
last_modified_at: 2024-10-16
related_topics:
  - title: English version
    url: /en/common/doctl-databases-replica.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/doctl-databases-replica.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># doctl databases replica

데이터베이스 클러스터와 연결된 읽기 전용 복제본을 관리.
더 많은 정보: <https://docs.digitalocean.com/reference/doctl/reference/databases/replica/>.

- 액세스 토큰을 사용하여 `doctl databases replica` 명령을 실행:

`doctl databases pool `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어</span>` --access-token `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">액세스_토큰</span>

- 읽기 전용 데이터베이스 복제본에 대한 정보를 검색:

`doctl databases replica get `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">데이터베이스_아이디</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">복제본_이름</span>

- 읽기 전용 데이터베이스 복제본 목록 검색:

`doctl databases replica list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">데이터베이스_아이디</span>

- 읽기 전용 데이터베이스 복제본 생성:

`doctl databases replica create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">데이터베이스_아이디</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">복제본_이름</span>

- 읽기 전용 데이터베이스 복제본 삭제:

`doctl databases replica delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">데이터베이스_아이디</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">복제본_이름</span>
