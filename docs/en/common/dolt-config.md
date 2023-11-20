---
layout: page
title: common/dolt-config (English)
description: "Read and write local (per repository) and global (per user) Dolt configuration variables."
content_hash: e9b5b45e49772a3ba9561d9b1e288a9aa5e9af95
last_modified_at: 2023-11-20
tldri18n_status: 2
---
# dolt config

Read and write local (per repository) and global (per user) Dolt configuration variables.
More information: <https://docs.dolthub.com/cli-reference/cli#dolt-config>.

- List all local and global configuration options and their values:

`dolt config --list`

- Display the value of a local or global configuration variable:

`dolt config --get `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>

- Modify the value of a local configuration variable, creating it if it doesn't exist:

`dolt config --add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">value</span>

- Modify the value of a global configuration variable, creating it if it doesn't exist:

`dolt config --global --add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">value</span>

- Delete a local configuration variable:

`dolt config --unset `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>

- Delete a global configuration variable:

`dolt config --global --unset `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>
