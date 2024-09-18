---
layout: page
title: linux/debchange (English)
description: "Mantain the debian/changelog file of a Debian source package."
content_hash: 698319134fc860d6e6d6375f17f83bcff8a9544d
last_modified_at: 2024-09-18
tldri18n_status: 2
---
# debchange

Mantain the debian/changelog file of a Debian source package.
More information: <https://manned.org/debchange.1>.

- Add a new version for a non-maintainer upload to the changelog:

`debchange --nmu`

- Add a changelog entry to the current version:

`debchange --append`

- Add a changelog entry to close the bug with specified ID:

`debchange --closes `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bug_id</span>
