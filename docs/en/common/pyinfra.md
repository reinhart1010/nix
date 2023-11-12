---
layout: page
title: common/pyinfra (English)
description: "Automates infrastructure at a large scale."
content_hash: 7255782118e2fff1acafd63ac6c2492866d474d2
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# pyinfra

Automates infrastructure at a large scale.
More information: <https://docs.pyinfra.com>.

- Execute a command over SSH:

`pyinfra `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">target_ip_address</span>` exec -- `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command_name_and_arguments</span>

- Execute contents of a deploy file on a list of targets:

`pyinfra `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/target_list.py</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/deploy.py</span>

- Execute commands on locally:

`pyinfra @local `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/deploy.py</span>

- Execute commands over Docker:

`pyinfra @docker/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">container</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/deploy.py</span>
