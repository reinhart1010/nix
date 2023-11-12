---
layout: page
title: common/ansible (English)
description: "Manage groups of computers remotely over SSH. (use the `/etc/ansible/hosts` file to add new groups/hosts)."
content_hash: 029463561852aedfe8c4c0aea9b186ac2f305cb0
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/ansible.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/ansible.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/ansible.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/ansible.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/ansible.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/ansible.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ansible

Manage groups of computers remotely over SSH. (use the `/etc/ansible/hosts` file to add new groups/hosts).
Some subcommands such as `ansible galaxy` have their own usage documentation.
More information: <https://www.ansible.com/>.

- List hosts belonging to a group:

`ansible `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">group</span>` --list-hosts`

- Ping a group of hosts by invoking the ping module:

`ansible `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">group</span>` -m ping`

- Display facts about a group of hosts by invoking the setup module:

`ansible `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">group</span>` -m setup`

- Execute a command on a group of hosts by invoking command module with arguments:

`ansible `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">group</span>` -m command -a '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">my_command</span>`'`

- Execute a command with administrative privileges:

`ansible `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">group</span>` --become --ask-become-pass -m command -a '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">my_command</span>`'`

- Execute a command using a custom inventory file:

`ansible `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">group</span>` -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">inventory_file</span>` -m command -a '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">my_command</span>`'`

- List the groups in an inventory:

`ansible localhost -m debug -a '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">var=groups.keys()</span>`'`
