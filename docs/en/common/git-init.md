---
layout: page
title: common/git-init (English)
description: "Initializes a new local Git repository."
content_hash: 71969f6fe395e0ff7b9a3f68f16b716ffc09c01f
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/git-init.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-init.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-init.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/common/git-init.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-init.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/git-init.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-init.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git init

Initializes a new local Git repository.
More information: <https://git-scm.com/docs/git-init>.

- Initialize a new local repository:

`git init`

- Initialize a repository with the specified name for the initial branch:

`git init --initial-branch=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">branch_name</span>

- Initialize a repository using SHA256 for object hashes (requires Git version 2.29+):

`git init --object-format=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sha256</span>

- Initialize a barebones repository, suitable for use as a remote over ssh:

`git init --bare`
