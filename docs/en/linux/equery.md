---
layout: page
title: linux/equery (English)
description: "View information about Portage packages."
content_hash: ab91073e7dbcf39937f30c4bdb6ca09133762361
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# equery

View information about Portage packages.
More information: <https://wiki.gentoo.org/wiki/Equery>.

- List all installed packages:

`equery list '*'`

- Search for installed packages in the Portage tree and in overlays:

`equery list -po `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package1 package2 ...</span>

- List all packages that depend on a given package:

`equery depends `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- List all packages that a given package depends on:

`equery depgraph `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- List all files installed by a package:

`equery files --tree `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>
