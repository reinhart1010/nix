---
layout: page
title: common/linode-cli-object-storage (한국어)
description: "Linode 오브젝트 스토리지 관리."
content_hash: be741c87f4ba9ff5897ec5bb1cbad842cb5af1c0
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/common/linode-cli-object-storage.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/linode-cli-object-storage.html
    icon: bi bi-globe
tldri18n_status: 2
---
# linode-cli object-storage

Linode 오브젝트 스토리지 관리.
같이 보기: `linode-cli`.
더 많은 정보: <https://techdocs.akamai.com/cloud-computing/docs/cli-commands-for-object-storage>.

- 모든 오브젝트 스토리지 버킷 나열:

`linode-cli object-storage buckets list`

- 새 오브젝트 스토리지 버킷 생성:

`linode-cli object-storage buckets create --cluster `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">클러스터_ID</span>` --label `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">버킷_레이블</span>

- 오브젝트 스토리지 버킷 삭제:

`linode-cli object-storage buckets delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">클러스터_ID</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">버킷_레이블</span>

- 오브젝트 스토리지 클러스터 지역 나열:

`linode-cli object-storage clusters list`

- 오브젝트 스토리지의 액세스 키 나열:

`linode-cli object-storage keys list`

- 오브젝트 스토리지에 대한 새 액세스 키 생성:

`linode-cli object-storage keys create --label `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">레이블</span>

- 오브젝트 스토리지에 대한 액세스 키 해제:

`linode-cli object-storage keys revoke `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">액세스_키_ID</span>
