---
layout: page
title: common/hg-update (English)
description: "Update the working directory to a specified changeset."
content_hash: 53fc353d21772318743dfe2043ae33096e39bcfe
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# hg update

Update the working directory to a specified changeset.
More information: <https://www.mercurial-scm.org/doc/hg.1.html#update>.

- Update to the tip of the current branch:

`hg update`

- Update to the specified revision:

`hg update --rev `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">revision</span>

- Update and discard uncommitted changes:

`hg update --clean`

- Update to the last commit matching a specified date:

`hg update --date `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dd-mm-yyyy</span>
