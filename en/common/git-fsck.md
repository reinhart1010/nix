---
layout: page
title: common/git-fsck (English)
description: "Verify the validity and connectivity of nodes in a Git repository index."
content_hash: 2a2eb4dabffdd34f5c3db21a772571749e5b543c
related_topics:
  - title: français version
    url: /fr/common/git-fsck.html
    icon: bi bi-globe
---
# git fsck

Verify the validity and connectivity of nodes in a Git repository index.
Does not make any modifications. See `git gc` for cleaning up dangling blobs.
More information: <https://git-scm.com/docs/git-fsck>.

- Check the current repository:

`git fsck`

- List all tags found:

`git fsck --tags`

- List all root nodes found:

`git fsck --root`
