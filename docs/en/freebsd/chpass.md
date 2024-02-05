---
layout: page
title: freebsd/chpass (English)
description: "Add or change user database information, including login shell and password."
content_hash: 963dc7f2029766964d51df4d8c1e424437ee2023
last_modified_at: 2024-02-05
tldri18n_status: 2
---
# chpass

Add or change user database information, including login shell and password.
See also: `passwd`.
More information: <https://man.freebsd.org/cgi/man.cgi?chpass>.

- Add or change user database information for the current user interactively:

`su -c chpass`

- Set a specific login [s]hell for the current user:

`chpass -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/shell</span>

- Set a login [s]hell for a specific user:

`chpass -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/shell</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>

- Change the account [e]xpire time (in seconds from the epoch, UTC):

`su -c 'chpass -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">time</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>`'`

- Change a user's password:

`su -c 'chpass -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">encrypted_password</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>`'`

- Specify the [h]ostname or address of an NIS server to query:

`su -c 'chpass -h `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hostname</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>`'`

- Specify a particular NIS [d]omain (system domain name by default):

`su -c 'chpass -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">domain</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>`'`
