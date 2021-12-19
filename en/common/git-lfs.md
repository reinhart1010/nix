---
layout: page
title: common/git-lfs (English)
description: "Work with large files in Git repositories."
content_hash: 16efba5eccac98f76518d9825b480ed7f677afd3
related_topics:
  - title: español version
    url: /es/common/git-lfs.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-lfs.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-lfs.html
    icon: bi bi-globe
---
# git lfs

Work with large files in Git repositories.
More information: <https://git-lfs.github.com>.

- Initialise Git LFS:

`git lfs install`

- Track files that match a glob:

`git lfs track '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.bin</span>`'`

- Change the Git LFS endpoint URL (useful if the LFS server is separate from the Git server):

`git config -f .lfsconfig lfs.url `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">lfs_endpoint_url</span>

- List tracked patterns:

`git lfs track`

- List tracked files that have been committed:

`git lfs ls-files`

- Push all Git LFS objects to the remote server (useful if errors are encountered):

`git lfs push --all `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">remote_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">branch_name</span>

- Fetch all Git LFS objects:

`git lfs fetch`

- Checkout all Git LFS objects:

`git lfs checkout`
