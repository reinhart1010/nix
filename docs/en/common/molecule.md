---
layout: page
title: common/molecule (English)
description: "Molecule helps testing Ansible roles."
content_hash: 209dafbeac648b0edf9a5f0805966057b7d0945d
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# molecule

Molecule helps testing Ansible roles.
More information: <https://molecule.readthedocs.io>.

- Create a new Ansible role:

`molecule init role --role-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">role_name</span>

- Run tests:

`molecule test`

- Start the instance:

`molecule create`

- Configure the instance:

`molecule converge`

- List scenarios of the instance:

`molecule matrix converge`

- Log in into the instance:

`molecule login`
