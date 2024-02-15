---
layout: page
title: common/git-check-ref-format (English)
description: "Check if a reference name is acceptable, and exit with a non-zero status if it is not."
content_hash: da2e9977e001a5ed1b6ad3c5566fcc524880f243
last_modified_at: 2024-02-15
related_topics:
  - title: Indonesia version
    url: /id/common/git-check-ref-format.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-check-ref-format.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git check-ref-format

Check if a reference name is acceptable, and exit with a non-zero status if it is not.
More information: <https://git-scm.com/docs/git-check-ref-format>.

- Check the format of the specified reference name:

`git check-ref-format `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">refs/head/refname</span>

- Print the name of the last branch checked out:

`git check-ref-format --branch @{-1}`

- Normalize a refname:

`git check-ref-format --normalize `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">refs/head/refname</span>
