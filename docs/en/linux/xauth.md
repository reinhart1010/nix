---
layout: page
title: linux/xauth (English)
description: "Edit and display the authorization information used in connecting to the X server."
content_hash: 7a3e149c745e87e9976d8bfd56b4d2cfb05b3589
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# xauth

Edit and display the authorization information used in connecting to the X server.
More information: <https://manned.org/xauth>.

- Start interactive mode with a specific authority file (defaults to `~/.Xauthority`):

`xauth -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Display information about the authority file:

`xauth info`

- Display authorization entries for all the displays:

`xauth list`

- Add an authorization for a specific display:

`xauth add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">display_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">protocol_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">key</span>

- Remove the authorization for a specific display:

`xauth remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">display_name</span>

- Print the authorization entry for the current display to `stdout`:

`xauth extract - $DISPLAY`

- Merge the authorization entries from a specific file into the authorization database:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>` | xauth merge -`

- Display help:

`xauth --help`
