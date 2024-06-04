---
layout: page
title: common/git-fsck (English)
description: "Verify the validity and connectivity of nodes in a Git repository index."
content_hash: 8c87c566383d168813c6c13373a35153df26c979
last_modified_at: 2024-06-04
related_topics:
  - title: français version
    url: /fr/common/git-fsck.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-fsck.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git fsck

Verify the validity and connectivity of nodes in a Git repository index.
Does not make any modifications.
See also: `git gc` for cleaning up dangling blobs.
More information: <https://git-scm.com/docs/git-fsck>.

- Check the current repository:

`git fsck`

- List all tags found:

`git fsck --tags`

- List all root nodes found:

`git fsck --root`
