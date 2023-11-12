---
layout: page
title: common/dvc-config (English)
description: "Low level command to manage custom configuration options for dvc repositories."
content_hash: b3ee42dd17492ed7824f54c70dea2a5092272dbd
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# dvc config

Low level command to manage custom configuration options for dvc repositories.
These configurations can be on project, local, global, or system level.
More information: <https://dvc.org/doc/command-reference/config>.

- Get the name of the default remote:

`dvc config core.remote`

- Set the project's default remote:

`dvc config core.remote `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">remote_name</span>

- Unset the project's default remote:

`dvc config --unset core.remote`

- Get the config value for a specified key for the current project:

`dvc config `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">key</span>

- Set the config value for a key on a project level:

`dvc config `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">key</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">value</span>

- Unset a project level config value for a given key:

`dvc config --unset `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">key</span>

- Set a local, global, or system level config value:

`dvc config --local/global/system `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">key</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">value</span>
