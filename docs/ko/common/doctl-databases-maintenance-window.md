---
layout: page
title: common/doctl-databases-maintenance-window (한국어)
description: "데이터베이스의 유지 관리 기간을 예약하고 일정을 확인."
content_hash: 3e866cbcc8a014139353f20d31a50af9489d2e88
last_modified_at: 2024-10-17
related_topics:
  - title: English version
    url: /en/common/doctl-databases-maintenance-window.html
    icon: bi bi-globe
tldri18n_status: 2
---
# doctl databases maintenance-window

데이터베이스의 유지 관리 기간을 예약하고 일정을 확인.
더 많은 정보: <https://docs.digitalocean.com/reference/doctl/reference/databases/maintenance-window>.

- 액세스 토큰을 사용하여 `doctl databases maintenance-window` 명령을 실행:

`doctl databases maintenance-window `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>` --access-token `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">액세스_토큰</span>

- 데이터베이스 클러스터의 유지 관리 기간에 대한 세부 정보를 검색:

`doctl databases maintenance-window get `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">데이터베이스_아이디</span>

- 데이터베이스 클러스터의 유지 관리 기간을 업데이트:

`doctl databases maintenance-window update `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">데이터베이스_아이디</span>` --day `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">요일</span>` --hour `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">24시간_형식의_시간</span>
