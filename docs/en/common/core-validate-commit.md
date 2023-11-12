---
layout: page
title: common/core-validate-commit (English)
description: "Validate commit messages for Node.js core."
content_hash: f9cc8ba1e8441796be4fd2f30a1132727ac2f3f4
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# core-validate-commit

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
