---
layout: page
title: common/git-secret (English)
description: "Stores private data inside a Git repository. Written in Bash."
content_hash: 13bf13a1b3957e658ee9a609db27144620b29433
last_modified_at: 2024-02-25
tldri18n_status: 2
---
# git secret

Stores private data inside a Git repository. Written in Bash.
More information: <https://github.com/sobolevn/git-secret>.

- Initialize `git-secret` in a local repository:

`git secret init`

- Grant access to the current Git user's email:

`git secret tell -m`

- Grant access by email:

`git secret tell `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">email</span>

- Revoke access by email:

`git secret killperson `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">email</span>

- List emails with access to secrets:

`git secret whoknows`

- Register a secret file:

`git secret add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Encrypt secrets:

`git secret hide`

- Decrypt secret files:

`git secret reveal`
