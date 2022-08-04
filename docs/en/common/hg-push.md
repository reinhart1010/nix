---
layout: page
title: common/hg-push (English)
description: "Push changes from the local repository to a specified destination."
content_hash: ec5abe6681ca0e237b6b154841a0e3a9527e5def
---
# hg push

Push changes from the local repository to a specified destination.
More information: <https://www.mercurial-scm.org/doc/hg.1.html#push>.

- Push changes to the "default" remote path:

`hg push`

- Push changes to a specified remote repository:

`hg push `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/destination_repository</span>

- Push a new branch if it does not exist (disabled by default):

`hg push --new-branch`

- Specify a specific revision changeset to push:

`hg push --rev `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">revision</span>

- Specify a specific branch to push:

`hg push --branch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">branch</span>

- Specify a specific bookmark to push:

`hg push --bookmark `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bookmark</span>
