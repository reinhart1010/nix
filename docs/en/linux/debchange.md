---
layout: page
title: linux/debchange (English)
description: "Tool for maintenance of the debian/changelog file in a Debian source package."
content_hash: f4fece26ddae31309509141c25f2111d6dff9d2e
last_modified_at: 2023-05-14
---
# debchange

Tool for maintenance of the debian/changelog file in a Debian source package.
More information: <https://manpages.debian.org/latest/devscripts/debchange.1.en.html>.

- Add a new version for a non-maintainer upload to the changelog:

`debchange --nmu`

- Add a changelog entry to the current version:

`debchange --append`

- Add a changelog entry to close the bug with specified ID:

`debchange --closes `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bug_id</span>
