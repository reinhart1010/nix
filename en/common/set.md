---
layout: page
title: common/set (English)
description: "Display, set or unset values of shell attributes and positional parameters."
content_hash: af6d6c90e5c707afc0b26c3506a6f985da485293
---
# set

Display, set or unset values of shell attributes and positional parameters.

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
