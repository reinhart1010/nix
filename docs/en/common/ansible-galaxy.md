---
layout: page
title: common/ansible-galaxy (English)
description: "Create and manage Ansible roles."
content_hash: 9526fa978985f217d2203498b2e1eaab3941e58e
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/ansible-galaxy.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/ansible-galaxy.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/ansible-galaxy.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/ansible-galaxy.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/ansible-galaxy.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ansible-galaxy

Create and manage Ansible roles.
More information: <https://docs.ansible.com/ansible/latest/cli/ansible-galaxy.html>.

- Install a role:

`ansible-galaxy install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>`.`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">role_name</span>

- Remove a role:

`ansible-galaxy remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>`.`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">role_name</span>

- List installed roles:

`ansible-galaxy list`

- Search for a given role:

`ansible-galaxy search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">role_name</span>

- Create a new role:

`ansible-galaxy init `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">role_name</span>

- Get information about a user role:

`ansible-galaxy role info `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>`.`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">role_name</span>

- Get information about a collection:

`ansible-galaxy collection info `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>`.`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">collection_name</span>
