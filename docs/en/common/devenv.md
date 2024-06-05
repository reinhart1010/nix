---
layout: page
title: common/devenv (English)
description: "Fast, Declarative, Reproducible and Composable Developer Environments using Nix."
content_hash: 53e729a9508bebbf3190f8e59b139523dc124d2c
last_modified_at: 2024-06-05
tldri18n_status: 2
---
# devenv

Fast, Declarative, Reproducible and Composable Developer Environments using Nix.
More information: <https://devenv.sh>.

- Initialise the environment:

`devenv init`

- Enter the Development Environment with relaxed hermeticity (state of being airtight):

`devenv shell --impure`

- Get detailed information about the current environment:

`devenv info --verbose`

- Start processes with `devenv`:

`devenv up --config /`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path</span>`/`

- Clean the environment variables and re-enter the shell in offline mode:

`devenv --clean --offline`

- Delete the previous shell generations:

`devenv gc`
