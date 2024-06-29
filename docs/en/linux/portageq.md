---
layout: page
title: linux/portageq (English)
description: "Query for information about Portage, the Gentoo Linux package manager."
content_hash: 4f374970b7d8339237558fc729b564a7f482b028
last_modified_at: 2024-06-29
tldri18n_status: 2
---
# portageq

Query for information about Portage, the Gentoo Linux package manager.
Queryable Portage-specific environment variables are listed in `/var/db/repos/gentoo/profiles/info_vars`.
More information: <https://wiki.gentoo.org/wiki/Portageq>.

- Display the value of a Portage-specific environment variable:

`portageq envvar `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">variable</span>

- Display a detailed list of repositories configured with Portage:

`portageq repos_config /`

- Display a list of repositories sorted by priority (highest first):

`portageq get_repos /`

- Display a specific piece of metadata about an atom (i.e. package name including the version):

`portageq metadata / `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ebuild|porttree|binary|...</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">category</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">BDEPEND|DEFINED_PHASES|DEPEND|...</span>
