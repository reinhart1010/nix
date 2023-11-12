---
layout: page
title: common/op (English)
description: "Official CLI for 1Password's desktop app."
content_hash: e970dbcd4ab57d77d991e8f99fdcdd774479f3ba
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# op

Official CLI for 1Password's desktop app.
More information: <https://developer.1password.com/docs/cli/reference>.

- Sign in to a 1Password account:

`op signin`

- List all vaults:

`op vault list`

- Print item details in JSON format:

`op item get `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">item_name</span>` --format json`

- Create a new item with a category in the default vault:

`op item create --category `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">category_name</span>

- Print a referenced secret to `stdout`:

`op read `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">secret_reference</span>

- Pass secret references from exported environment variables to a command:

`op run -- `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>

- Pass secret references from an environment file to a command:

`op run --env-file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/env_file.env</span>` -- `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>

- Read secret references from a file and save plaintext secrets to a file:

`op inject --in-file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input_file</span>` --out-file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output_file</span>
