---
layout: page
title: netbsd/chpass (English)
description: "Add or change user database information, including login shell and password."
content_hash: 2adec823fdeddc2b5bf2c351a3848e0491850f98
last_modified_at: 2024-02-05
tldri18n_status: 2
---
# chpass

Add or change user database information, including login shell and password.
See also: `passwd`.
More information: <https://man.openbsd.org/chsh>.

- Set a specific login shell for the current user interactively:

`su -c chpass`

- Set a specific login [s]hell for the current user:

`chpass -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/shell</span>

- Set a login [s]hell for a specific user:

`chpass chsh -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/shell</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>

- Specify a user database entry in the `passwd` file format:

`su -c 'chpass -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username:encrypted_password:uid:gid:...</span>` -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>`' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>

- Only update the [l]ocal password file:

`su -c 'chpass -l -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/shell</span>`' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>

- Forcedly change the database [y]P password database entry:

`su -c 'chpass -y -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/shell</span>`' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>
