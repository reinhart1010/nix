---
layout: page
title: common/git-check-ref-format (English)
description: "Check if a given refname is acceptable, and exit with a non-zero status if it is not."
content_hash: e7e7ec4d6d7dc5ea38a51adb6750240e3ecb957e
last_modified_at: 2023-11-15
related_topics:
  - title: Türkçe version
    url: /tr/common/git-check-ref-format.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git check-ref-format

Check if a given refname is acceptable, and exit with a non-zero status if it is not.
More information: <https://git-scm.com/docs/git-check-ref-format>.

- Check the format of the specified refname:

`git check-ref-format `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">refs/head/refname</span>

- Print the name of the last branch checked out:

`git check-ref-format --branch @{-1}`

- Normalize a refname:

`git check-ref-format --normalize `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">refs/head/refname</span>
