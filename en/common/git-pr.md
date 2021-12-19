---
layout: page
title: common/git-pr (English)
description: "Check out GitHub pull requests locally."
content_hash: e505c7b5168e48324623927cf081be45766f33d5
related_topics:
  - title: español version
    url: /es/common/git-pr.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-pr.html
    icon: bi bi-globe
---
# git pr

Check out GitHub pull requests locally.
More information: <https://github.com/tj/git-extras/blob/master/Commands.md#git-pr>.

- Check out a specific pull request:

`git pr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pr_number</span>

- Check out a pull request for a specific remote:

`git pr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pr_number</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">remote</span>

- Check out a pull request from its URL:

`git pr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>

- Clean up old pull request branches:

`git pr clean`
