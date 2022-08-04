---
layout: page
title: common/git-pr (English)
description: "Check out GitHub pull requests locally."
content_hash: c182d9e84e1cd6570f7a42551dbf69ac5978d5d6
related_topics:
  - title: español version
    url: /es/common/git-pr.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-pr.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-pr.html
    icon: bi bi-globe
---
# git pr

Check out GitHub pull requests locally.
Part of `git-extras`.
More information: <https://github.com/tj/git-extras/blob/master/Commands.md#git-pr>.

- Check out a specific pull request:

`git pr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pr_number</span>

- Check out a pull request from a specific remote:

`git pr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pr_number</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">remote</span>

- Check out a pull request from its URL:

`git pr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>

- Clean up old pull request branches:

`git pr clean`
