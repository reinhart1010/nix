---
layout: page
title: common/secrethub (English)
description: "A tool to keep secrets out of config files."
content_hash: b0f0419197d52232378aac231fbdf5b57257ecb5
---
# secrethub

A tool to keep secrets out of config files.
More information: <https://secrethub.io>.

- Print a secret to stdout:

`secrethub read `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/secret</span>

- Generate a random value and store it as a new or updated secret:

`secrethub generate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/secret</span>

- Store a value from the clipboard as a new or updated secret:

`secrethub write --clip `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/secret</span>

- Store a value supplied on stdin as a new or updated secret:

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">secret_value</span>`" | secrethub write `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/secret</span>

- Audit a repository or secret:

`secrethub audit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/repo_or_secret</span>
