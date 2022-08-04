---
layout: page
title: common/git-flow (English)
description: "A collection of Git extensions to provide high-level repository operations."
content_hash: 9d77b55ac099c5e612439ccc4c314128841542cc
related_topics:
  - title: français version
    url: /fr/common/git-flow.html
    icon: bi bi-globe
---
# git flow

A collection of Git extensions to provide high-level repository operations.
More information: <https://github.com/nvie/gitflow>.

- Initialize it inside an existing Git repository:

`git flow init`

- Start developing on a feature branch based on `develop`:

`git flow feature start `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">feature</span>

- Finish development on a feature branch, merging it into the `develop` branch and deleting it:

`git flow feature finish `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">feature</span>

- Publish a feature to the remote server:

`git flow feature publish `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">feature</span>

- Get a feature published by another user:

`git flow feature pull origin `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">feature</span>
