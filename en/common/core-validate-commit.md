---
layout: page
title: common/core-validate-commit (English)
description: "Validate commit messages for Node.js core."
content_hash: f9cc8ba1e8441796be4fd2f30a1132727ac2f3f4
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># core-validate-commit

Validate commit messages for Node.js core.
More information: <https://github.com/nodejs/core-validate-commit>.

- Validate the current commit:

`core-validate-commit`

- Validate a specific commit:

`core-validate-commit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commit_hash</span>

- Validate a range of commits:

`git rev-list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commit_hash</span>`..HEAD | xargs core-validate-commit`

- List all validation rules:

`core-validate-commit --list`

- List all valid Node.js subsystems:

`core-validate-commit --list-subsystem`

- Validate the current commit formatting the output in tap format:

`core-validate-commit --tap`

- Display help:

`core-validate-commit --help`
