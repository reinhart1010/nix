---
layout: page
title: common/linode-cli-volumes (한국어)
description: "Linode 볼륨 관리."
content_hash: ce8c8dacc59ab0da35ca508dec871eb7f6900145
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/common/linode-cli-volumes.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/linode-cli-volumes.html
    icon: bi bi-globe
tldri18n_status: 2
---
# linode-cli volumes

Linode 볼륨 관리.
같이 보기: `linode-cli`.
더 많은 정보: <https://techdocs.akamai.com/cloud-computing/docs/cli-commands-for-block-storage-volumes>.

- 현재 볼륨 나열:

`linode-cli volumes list`

- 새 볼륨 생성 및 특정 Linode에 연결:

`linode-cli volumes create --label `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">볼륨_레이블</span>` --size `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">크기_GB</span>` --linode-id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">linode_id</span>

- 특정 Linode에 볼륨 연결:

`linode-cli volumes attach `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">볼륨_id</span>` --linode-id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">linode_id</span>

- Linode에서 볼륨 분리:

`linode-cli volumes detach `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">볼륨_id</span>

- 볼륨 크기 조정 (참고: 크기만 증가 가능):

`linode-cli volumes resize `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">볼륨_id</span>` --size `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">새_크기_GB</span>

- 볼륨 삭제:

`linode-cli volumes delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">볼륨_id</span>
