---
layout: page
title: common/git-secret (English)
description: "Bash tool which stores private data inside a Git repository."
content_hash: 779e778e8af8b0ac8ca09c2b2119f2ae4cdcc857
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# git secret

Bash tool which stores private data inside a Git repository.
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
