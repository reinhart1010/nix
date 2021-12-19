---
layout: page
title: common/git-reflog (English)
description: "Show a log of changes to local references like HEAD, branches or tags."
content_hash: 5b69ab1bb4907e456d0b62b3d80e28dbe9210dc6
related_topics:
  - title: español version
    url: /es/common/git-reflog.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-reflog.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-reflog.html
    icon: bi bi-globe
---
# git reflog

Show a log of changes to local references like HEAD, branches or tags.
More information: <https://git-scm.com/docs/git-reflog>.

- Show the reflog for HEAD:

`git reflog`

- Show the reflog for a given branch:

`git reflog `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">branch_name</span>

- Show only the 5 latest entries in the reflog:

`git reflog -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5</span>
