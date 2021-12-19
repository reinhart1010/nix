---
layout: page
title: common/git-describe (English)
description: "Give an object a human-readable name based on an available ref."
content_hash: 03a9d67031de9a77ae867c5c237f4aca29758aba
related_topics:
  - title: français version
    url: /fr/common/git-describe.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-describe.html
    icon: bi bi-globe
---
# git describe

Give an object a human-readable name based on an available ref.
More information: <https://git-scm.com/docs/git-describe>.

- Create a unique name for the current commit (the name contains the most recent annotated tag, the number of additional commits, and the abbreviated commit hash):

`git describe`

- Create a name with 4 digits for the abbreviated commit hash:

`git describe --abbrev=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">4</span>

- Generate a name with the tag reference path:

`git describe --all`

- Describe a Git tag:

`git describe `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">v1.0.0</span>

- Create a name for the last commit of a given branch:

`git describe `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">branch_name</span>
