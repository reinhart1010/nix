---
layout: page
title: common/set (English)
description: "Display, set or unset values of shell attributes and positional parameters."
content_hash: 80b7d3b2ede8426fcdb261266a71bd35a1b077ad
last_modified_at: 2023-12-29
tldri18n_status: 2
---
# set

Display, set or unset values of shell attributes and positional parameters.
More information: <https://pubs.opengroup.org/onlinepubs/9699919799/utilities/V3_chap02.html#set>.

- Display the names and values of shell variables:

`set`

- Mark variables that are modified or created for export:

`set -a`

- Notify of job termination immediately:

`set -b`

- Set various options, e.g. enable `vi` style line editing:

`set -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vi</span>

- Set the shell to exit as soon as the first error is encountered (mostly used in scripts):

`set -e`
