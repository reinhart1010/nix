---
layout: page
title: linux/runcon (English)
description: "Run a program in a different SELinux security context."
content_hash: e8a085897ad68d78715ecc76e59603598673bf91
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# runcon

Run a program in a different SELinux security context.
With neither context nor command, print the current security context.
More information: <https://www.gnu.org/software/coreutils/runcon>.

- Determine the current domain:

`runcon`

- Specify the domain to run a command in:

`runcon -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">domain</span>`_t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>

- Specify the context role to run a command with:

`runcon -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">role</span>`_r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>

- Specify the full context to run a command with:

`runcon `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">user</span>`_u:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">role</span>`_r:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">domain</span>`_t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>
