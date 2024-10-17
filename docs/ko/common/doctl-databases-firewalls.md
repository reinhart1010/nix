---
layout: page
title: common/doctl-databases-firewalls (한국어)
description: "데이터베이스 클러스터의 방화벽을 관리."
content_hash: c265a1c108859393af8de6320e975da96722265c
last_modified_at: 2024-10-17
related_topics:
  - title: English version
    url: /en/common/doctl-databases-firewalls.html
    icon: bi bi-globe
tldri18n_status: 2
---
# doctl databases firewalls

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
