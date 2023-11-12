---
layout: page
title: common/ansible-inventory (English)
description: "Display or dump an Ansible inventory."
content_hash: a802d407ddd26291e485f1435fed9865b73c939d
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/ansible-inventory.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/ansible-inventory.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/ansible-inventory.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ansible-inventory

Display or dump an Ansible inventory.
See also: `ansible`.
More information: <https://docs.ansible.com/ansible/latest/cli/ansible-inventory.html>.

- Display the default inventory:

`ansible-inventory --list`

- Display a custom inventory:

`ansbile-inventory --list --inventory `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file_or_script_or_directory</span>

- Display the default inventory in YAML:

`ansible-inventory --list --yaml`

- Dump the default inventory to a file:

`ansible-inventory --list --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>
