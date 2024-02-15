---
layout: page
title: linux/debchange (English)
description: "Mantain the debian/changelog file of a Debian source package."
content_hash: 8b275ccf2a9ff4c9f8e8bbf3005eefb27f62e402
last_modified_at: 2024-02-15
tldri18n_status: 2
---
# debchange

Mantain the debian/changelog file of a Debian source package.
More information: <https://manpages.debian.org/latest/devscripts/debchange.1.en.html>.

- Add a new version for a non-maintainer upload to the changelog:

`debchange --nmu`

- Add a changelog entry to the current version:

`debchange --append`

- Add a changelog entry to close the bug with specified ID:

`debchange --closes `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bug_id</span>
