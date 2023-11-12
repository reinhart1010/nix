---
layout: page
title: common/transcrypt (English)
description: "Transparently encrypt files within a Git repository."
content_hash: 8790cabb153cd7c4788d1cf879afa363bf379b10
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# transcrypt

Transparently encrypt files within a Git repository.
More information: <https://github.com/elasticdog/transcrypt>.

- Initialize an unconfigured repository:

`transcrypt`

- List the currently encrypted files:

`git ls-crypt`

- Display the credentials of a configured repository:

`transcrypt --display`

- Initialize and decrypt a fresh clone of a configured repository:

`transcrypt --cipher=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cipher</span>

- Rekey to change the encryption cipher or password:

`transcrypt --rekey`
