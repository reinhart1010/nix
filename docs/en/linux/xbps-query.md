---
layout: page
title: linux/xbps-query (English)
description: "XBPS utility to query for package and repository information."
content_hash: 739d40d2b2816e4c94217b11af353834d4a76d0a
last_modified_at: 2024-09-25
related_topics:
  - title: Nederlands version
    url: /nl/linux/xbps-query.html
    icon: bi bi-globe
tldri18n_status: 2
---
# xbps-query

XBPS utility to query for package and repository information.
See also: `xbps`.
More information: <https://manned.org/xbps-query.1>.

- Search for a package in remote repositories using a regular expression or a keyword (if `--regex` is omitted):

`xbps-query --search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">regular_expression|keyword</span>` --repository --regex`

- Show information about an installed package:

`xbps-query --show `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- Show information about a package in remote repositories:

`xbps-query --show `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>` --repository`

- List packages registered in the package database:

`xbps-query --list-pkgs`

- List explicitly installed packages (i.e. not automatically installed as dependencies):

`xbps-query --list-manual-pkgs`
