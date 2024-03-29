---
layout: page
title: common/dvc-config (English)
description: "Low level command to manage custom configuration options for dvc repositories."
content_hash: d398cf22ea4db9b4200fcd24edf4a3db6dff3db5
last_modified_at: 2024-02-09
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

- Get the configuration value for a specified key for the current project:

`dvc config `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">key</span>

- Set the configuration value for a key on a project level:

`dvc config `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">key</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">value</span>

- Unset a project level configuration value for a given key:

`dvc config --unset `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">key</span>

- Set a local, global, or system level configuration value:

`dvc config --`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">local|global|system</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">key</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">value</span>
