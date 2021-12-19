---
layout: page
title: common/hg-pull (English)
description: "Pull changes from a specified repository to the local repository."
content_hash: e59c4708f253f2b76df26c4a5a52a3e813a825ab
---
# hg pull

Pull changes from a specified repository to the local repository.
More information: <https://www.mercurial-scm.org/doc/hg.1.html#pull>.

- Pull from the "default" source path:

`hg pull`

- Pull from a specified source repository:

`hg pull `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/source_repository</span>

- Update the local repository to the head of the remote:

`hg pull --update`

- Pull changes even when the remote repository is unrelated:

`hg pull --force`

- Specify a specific revision changeset to pull up to:

`hg pull --rev `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">revision</span>

- Specify a specific branch to pull:

`hg pull --branch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">branch</span>

- Specify a specific bookmark to pull:

`hg pull --bookmark `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bookmark</span>
