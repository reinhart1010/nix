---
layout: page
title: common/doas (English)
description: "Executes a command as another user."
content_hash: 2def708bfbb4e98e1ee1c03ca6e9aa74587e0b41
last_modified_at: 2024-01-25
tldri18n_status: 2
---
# doas

Executes a command as another user.
More information: <https://man.openbsd.org/doas>.

- Run a command as root:

`doas `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>

- Run a command as another user:

`doas -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">user</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>

- Launch the default shell as root:

`doas -s`

- Parse a configuration file and check if the execution of a command as another user is allowed:

`doas -C `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">config_file</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>

- Make `doas` request a password even after it was supplied earlier:

`doas -L`
