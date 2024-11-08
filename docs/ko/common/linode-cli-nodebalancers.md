---
layout: page
title: common/linode-cli-nodebalancers (한국어)
description: "Linode NodeBalancer 관리."
content_hash: de1388e155e05b9062ecf0322d2817d3781db894
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/common/linode-cli-nodebalancers.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/linode-cli-nodebalancers.html
    icon: bi bi-globe
tldri18n_status: 2
---
# linode-cli nodebalancers

Linode NodeBalancer 관리.
같이 보기: `linode-cli`.
더 많은 정보: <https://techdocs.akamai.com/cloud-computing/docs/cli-commands-for-nodebalancers>.

- 모든 NodeBalancer 나열:

`linode-cli nodebalancers list`

- 새 NodeBalancer 생성:

`linode-cli nodebalancers create --region `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">지역</span>

- 특정 NodeBalancer의 세부 정보 보기:

`linode-cli nodebalancers view `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nodebalancer_id</span>

- 기존 NodeBalancer 업데이트:

`linode-cli nodebalancers update `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nodebalancer_id</span>` --label `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">새_라벨</span>

- NodeBalancer 삭제:

`linode-cli nodebalancers delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nodebalancer_id</span>

- NodeBalancer의 구성 목록 나열:

`linode-cli nodebalancers configs list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nodebalancer_id</span>

- NodeBalancer에 새 구성 추가:

`linode-cli nodebalancers configs create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nodebalancer_id</span>` --port `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">포트</span>` --protocol `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">프로토콜</span>
