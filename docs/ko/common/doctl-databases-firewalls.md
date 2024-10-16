---
layout: page
title: common/doctl-databases-firewalls (한국어)
description: "데이터베이스 클러스터의 방화벽을 관리."
content_hash: c265a1c108859393af8de6320e975da96722265c
last_modified_at: 2024-10-16
related_topics:
  - title: English version
    url: /en/common/doctl-databases-firewalls.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/doctl-databases-firewalls.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># doctl databases firewalls

데이터베이스 클러스터의 방화벽을 관리.
더 많은 정보: <https://docs.digitalocean.com/reference/doctl/reference/databases/firewalls>.

- 액세스 토큰을 사용하여 `doctl databases firewalls` 명령을 실행:

`doctl databases firewalls `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어</span>` --access-token `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">액세스_토큰</span>

- 특정 데이터베이스에 대한 방화벽 규칙 목록을 검색:

`doctl databases firewalls list`

- 특정 데이터베이스에 데이터베이스 방화벽 규칙을 추가:

`doctl databases firewalls append `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">데이터베이스_아이디</span>` --rule `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">droplet|k8s|ip_addr|tag|app</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">value</span>

- 특정 데이터베이스에 대한 방화벽 규칙을 추가:

`doctl databases firewalls remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">데이터베이스_아이디</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">룰_uuid</span>
