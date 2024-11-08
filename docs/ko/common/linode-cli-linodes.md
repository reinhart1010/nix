---
layout: page
title: common/linode-cli-linodes (한국어)
description: "Linode 인스턴스를 관리."
content_hash: 92823330d74b08fc490e4846235dde8e2e8bb56d
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/common/linode-cli-linodes.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/linode-cli-linodes.html
    icon: bi bi-globe
tldri18n_status: 2
---
# linode-cli linodes

Linode 인스턴스를 관리.
같이 보기: `linode-cli`.
더 많은 정보: <https://techdocs.akamai.com/cloud-computing/docs/cli-commands-for-compute-instances>.

- 모든 Linode 나열:

`linode-cli linodes list`

- 새 Linode 생성:

`linode-cli linodes create --type `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">linode_유형</span>` --region `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">지역</span>` --image `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이미지_ID</span>

- 특정 Linode의 세부 정보 보기:

`linode-cli linodes view `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">linode_ID</span>

- Linode 설정 업데이트:

`linode-cli linodes update `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">linode_ID</span>` --label `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">새_레이블</span>

- Linode 삭제:

`linode-cli linodes delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">linode_ID</span>

- Linode에 전원 관리 작업 수행:

`linode-cli linodes `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">boot|reboot|shutdown</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">linode_ID</span>

- Linode에 대한 사용 가능한 백업 목록:

`linode-cli linodes backups-list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">linode_ID</span>

- Linode에 백업 복원:

`linode-cli linodes backups-restore `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">linode_ID</span>` --backup-id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">백업_ID</span>
