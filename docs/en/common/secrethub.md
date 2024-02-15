---
layout: page
title: common/secrethub (English)
description: "Keep secrets out of config files."
content_hash: faed5d15e0ed8fdbe3c4d996c98355bef452c4fd
last_modified_at: 2024-02-15
tldri18n_status: 2
---
# secrethub

Keep secrets out of config files.
More information: <https://secrethub.io>.

- Print a secret to `stdout`:

`secrethub read `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/secret</span>

- Generate a random value and store it as a new or updated secret:

`secrethub generate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/secret</span>

- Store a value from the clipboard as a new or updated secret:

`secrethub write --clip `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/secret</span>

- Store a value supplied on `stdin` as a new or updated secret:

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">secret_value</span>`" | secrethub write `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/secret</span>

- Audit a repository or secret:

`secrethub audit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/repo_or_secret</span>
