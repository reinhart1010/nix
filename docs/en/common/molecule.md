---
layout: page
title: common/molecule (English)
description: "Molecule helps testing Ansible roles."
content_hash: b030f0a4e145d28cdaf4e7a3fd2bc3af3c34ce27
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

- Log in into the instance:

`molecule login`
