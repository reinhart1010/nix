---
layout: page
title: linux/slapt-src (English)
description: "A utility to automate building of slackbuilds."
content_hash: e1cc1ddbbfdbf3b5a650bd0e4a8af606e8d0b75e
---
# slapt-src

A utility to automate building of slackbuilds.
SlackBuild sources need to be configured in the slapt-srcrc file.
More information: <https://github.com/jaos/slapt-src>.

- Update the list of available slackbuilds and versions:

`slapt-src --update`

- List all available slackbuilds:

`slapt-src --list`

- Fetch, build and install the specified slackbuild(s):

`slapt-src --install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">slackbuild_name</span>

- Locate slackbuilds by their name or description:

`slapt-src --search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">search_term</span>

- Display information about a slackbuild:

`slapt-src --show `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">slackbuild_name</span>
