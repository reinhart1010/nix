---
layout: page
title: common/ansible-inventory (한국어)
description: "Ansible 인벤토리를 표시하거나 덤프."
content_hash: 6f7654e9bf7149d1b72f63ed055d2cb066199720
last_modified_at: 2024-09-08
related_topics:
  - title: Deutsch version
    url: /de/common/ansible-inventory.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/ansible-inventory.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/ansible-inventory.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/ansible-inventory.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/ansible-inventory.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ansible-inventory

Ansible 인벤토리를 표시하거나 덤프.
또한, `ansible`을 참조하세요.
더 많은 정보: <https://docs.ansible.com/ansible/latest/cli/ansible-inventory.html>.

- 기본 인벤토리를 표시:

`ansible-inventory --list`

- 사용자 지정 인벤토리를 표시:

`ansible-inventory --list --inventory `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일_또는_스크립트_또는_디렉토리</span>

- YAML에서 기본 인벤토리를 표시:

`ansible-inventory --list --yaml`

- 기본 인벤토리를 파일에 덤프:

`ansible-inventory --list --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>
