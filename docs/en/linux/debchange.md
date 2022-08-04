---
layout: page
title: linux/debchange (English)
description: "Tool for maintenance of the debian/changelog file in a Debian source package."
content_hash: 4fb0c805ad3f56177a7acdbedfe565e7e03750fa
---
# debchange

Tool for maintenance of the debian/changelog file in a Debian source package.
More information: <https://manpages.debian.org/debchange>.

- Add a new version for a non-maintainer upload to the changelog:

`debchange --nmu`

- Add a changelog entry to the current version:

`debchange --append`

- Add a changelog entry to close the bug with specified ID:

`debchange --closes `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bug_id</span>
