---
layout: page
title: openbsd/chpass (English)
description: "Add or change user database information, including login shell and password."
content_hash: 12216a580487bf4a736669ee27011c284b6fbb6d
last_modified_at: 2024-02-05
tldri18n_status: 2
---
# chpass

Add or change user database information, including login shell and password.
See also: `passwd`.
More information: <https://man.openbsd.org/chsh>.

- Set a specific login shell for the current user interactively:

`doas chsh`

- Set a specific login [s]hell for the current user:

`doas chsh -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/shell</span>

- Set a login [s]hell for a specific user:

`doas chsh -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/shell</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>

- Specify a user database entry in the `passwd` file format:

`doas chsh -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username:encrypted_password:uid:gid:...</span>
