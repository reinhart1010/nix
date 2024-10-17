---
layout: page
title: common/doctl-databases-user (한국어)
description: "데이터베이스 사용자에 대한 세부 정보를 보고 생성."
content_hash: 9b5e9b362651012f898747967474f61010c20bed
last_modified_at: 2024-10-17
related_topics:
  - title: English version
    url: /en/common/doctl-databases-user.html
    icon: bi bi-globe
tldri18n_status: 2
---
# doctl databases user

데이터베이스 사용자에 대한 세부 정보를 보고 생성.
더 많은 정보: <https://docs.digitalocean.com/reference/doctl/reference/databases/user>.

- 액세스 토큰을 사용하여 `doctl databases user` 명령을 실행:

`doctl databases user `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어</span>` --access-token `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">access_token</span>

- 데이터베이스 사용자에 대한 세부 정보를 검색:

`doctl databases user get `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">데이터베이스_아이디</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자_이름</span>

- 특정 데이터베이스에 대한 데이터베이스 사용자 목록을 검색:

`doctl databases user list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">데이터베이스_아이디</span>

- 특정 사용자의 인증 비밀번호를 재설정:

`doctl databases user reset `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">데이터베이스_아이디</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자_이름</span>

- 특정 사용자에 대한 MySQL 인증 플러그인 재설정:

`doctl databases user reset `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">데이터베이스_아이디</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자_이름</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caching_sha2_password|mysql_native_password</span>

- 주어진 사용자 이름으로 주어진 데이터베이스에 사용자를 생성:

`doctl databases user create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">데이터베이스_아이디</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자_이름</span>

- 주어진 사용자 이름을 가진 주어진 데이터베이스에서 사용자를 삭제:

`doctl databases user delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">데이터베이스_아이디</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자_이름</span>
