---
layout: page
title: common/ansible-pull (한국어)
description: "VCS 저장소에서 Ansible 플레이북을 가져와 로컬 호스트에서 실행."
content_hash: 3d6f6884d625d96362f40a6301b6d9b2c27be5f7
last_modified_at: 2024-09-08
related_topics:
  - title: Deutsch version
    url: /de/common/ansible-pull.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/ansible-pull.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/ansible-pull.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/ansible-pull.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/ansible-pull.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ansible-pull

VCS 저장소에서 Ansible 플레이북을 가져와 로컬 호스트에서 실행.
더 많은 정보: <https://docs.ansible.com/ansible/latest/cli/ansible-pull.html>.

- VCS에서 플레이북을 가져와 기본 local.yml playbook을 실행:

`ansible-pull -U `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">저장소_url</span>

- VCS에서 플레이북을 가져와 특정 플레이북을 실행:

`ansible-pull -U `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">저장소_url</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">playbook</span>

- 특정 지점의 VCS에서 플레이북을 가져와 특정 플레이북을 실행:

`ansible-pull -U `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">저장소_url</span>` -C `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">branch</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">playbook</span>

- VCS에서 플레이북을 가져오고, 호스트 파일을 지정하고 특정 플레이북을 실행:

`ansible-pull -U `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">저장소_url</span>` -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hosts_file</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">playbook</span>
