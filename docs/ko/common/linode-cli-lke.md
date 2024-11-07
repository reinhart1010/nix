---
layout: page
title: common/linode-cli-lke (한국어)
description: "Linode Kubernetes Engine (LKE) 클러스터 관리."
content_hash: f5010bc45a7a95e6797a64023987e4f1d5696e49
last_modified_at: 2024-11-07
related_topics:
  - title: English version
    url: /en/common/linode-cli-lke.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/linode-cli-lke.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/linode-cli-lke.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># linode-cli lke

Linode Kubernetes Engine (LKE) 클러스터 관리.
같이 보기: `linode-cli`.
더 많은 정보: <https://techdocs.akamai.com/cloud-computing/docs/cli-commands-for-lke>.

- 모든 LKE 클러스터 나열:

`linode-cli lke clusters list`

- 새 LKE 클러스터 생성:

`linode-cli lke clusters create --region `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">지역</span>` --type `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">유형</span>` --node-type `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">노드_유형</span>` --nodes-count `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">수량</span>

- 특정 LKE 클러스터 세부정보 보기:

`linode-cli lke clusters view `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">클러스터_ID</span>

- 기존 LKE 클러스터 업데이트:

`linode-cli lke clusters update `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">클러스터_ID</span>` --node-type `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">새_노드_유형</span>

- LKE 클러스터 삭제:

`linode-cli lke clusters delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">클러스터_ID</span>
