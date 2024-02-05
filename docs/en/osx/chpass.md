---
layout: page
title: osx/chpass (English)
description: "Add or change user database information, including login shell and password."
content_hash: 5edb7298eceaa8661f6bbbd87227fcbb57cc2772
last_modified_at: 2024-02-05
tldri18n_status: 2
---
# chpass

Add or change user database information, including login shell and password.
Note: it's not possible to change the user's password on Open Directory systems, use `passwd` instead.
See also: `passwd`.
More information: <https://man.freebsd.org/cgi/man.cgi?chpass>.

- Add or change user database information for the current user interactively:

`su -c chpass`

- Set a specific login [s]hell for the current user:

`chpass -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/shell</span>

- Set a login [s]hell for a specific user:

`chpass -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/shell</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>

- Edit the user record on the directory node at the given [l]ocation:

`chpass -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">location</span>` -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/shell</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>

- Use the given [u]sername when authenticating to the directory node containing the user:

`chpass -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">authname</span>` -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/shell</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>
