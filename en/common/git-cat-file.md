---
layout: page
title: common/git-cat-file (English)
description: "Provide content or type and size information for Git repository objects."
content_hash: 3b89fad0dd99b1faae4af8e8d39a71e8cf2d42b4
related_topics:
  - title: français version
    url: /fr/common/git-cat-file.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-cat-file.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/git-cat-file.html
    icon: bi bi-globe
---
# git cat-file

Provide content or type and size information for Git repository objects.
More information: <https://git-scm.com/docs/git-cat-file>.

- Get the [s]ize of the HEAD commit in bytes:

`git cat-file -s HEAD`

- Get the [t]ype (blob, tree, commit, tag) of a given Git object:

`git cat-file -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">8c442dc3</span>

- Pretty-[p]rint the contents of a given Git object based on its type:

`git cat-file -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">HEAD~2</span>
