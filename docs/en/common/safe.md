---
layout: page
title: common/safe (English)
description: "Interact with HashiCorp Vault."
content_hash: 880de94eeb30d9a6eb48d32573337c43a8502a38
last_modified_at: 2023-07-16
---
# safe

Interact with HashiCorp Vault.
More information: <https://github.com/starkandwayne/safe>.

- Add a safe target:

`safe target `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vault_addr</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">target_name</span>

- Authenticate the CLI client against the Vault server, using an authentication token:

`safe auth `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">authentication_token</span>

- Print the environment variables describing the current target:

`safe env`

- Display a tree hierarchy of all reachable keys for a given path:

`safe tree `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path</span>

- Move a secret from one path to another:

`safe move `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">old/path/to/secret</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">new/path/to/secret</span>

- Generate a new 2048-bit SSH key-pair and store it:

`safe ssh `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2048</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/secret</span>

- Set non-sensitive keys for a secret:

`safe set `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/secret</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">key</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">value</span>

- Set auto-generated password in a secret:

`safe gen `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/secret</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">key</span>
