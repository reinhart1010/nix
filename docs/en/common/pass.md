---
layout: page
title: common/pass (English)
description: "Tool for storing and reading passwords or other sensitive data."
content_hash: 6708e0e83f154b0e4ed1f00f65fc6343ebcb8f54
related_topics:
  - title: Deutsch version
    url: /de/common/pass.html
    icon: bi bi-globe
---
# pass

Tool for storing and reading passwords or other sensitive data.
All data is GPG-encrypted, and managed with a Git repository.
More information: <https://www.passwordstore.org>.

- Initialize (or re-encrypt) the storage using one or more GPG IDs:

`pass init `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gpg_id_1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gpg_id_2</span>

- Save a new password and additional information (press Ctrl + D on a new line to complete):

`pass insert --multiline `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/data</span>

- Edit an entry:

`pass edit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/data</span>

- Copy a password (first line of the data file) to the clipboard:

`pass -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/data</span>

- List the whole store tree:

`pass`

- Generate a new random password with a given length, and copy it to the clipboard:

`pass generate -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/data</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">num</span>

- Initialize a new Git repository (any changes done by pass will be committed automatically):

`pass git init`

- Run a Git command on behalf of the password storage:

`pass git `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>
