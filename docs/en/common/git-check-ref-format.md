---
layout: page
title: common/git-check-ref-format (English)
description: "Checks if a given refname is acceptable, and exits with a non-zero status if it is not."
content_hash: 01b9c8da01dcaea135e25659a41b94a8b40f1ea2
---
# git check-ref-format

Checks if a given refname is acceptable, and exits with a non-zero status if it is not.
More information: <https://git-scm.com/docs/git-check-ref-format>.

- Check the format of the specified refname:

`git check-ref-format `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">refs/head/refname</span>

- Print the name of the last branch checked out:

`git check-ref-format --branch @{-1}`

- Normalize a refname:

`git check-ref-format --normalize `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">refs/head/refname</span>
