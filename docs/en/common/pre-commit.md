---
layout: page
title: common/pre-commit (English)
description: "Create Git hooks that get run before a commit."
content_hash: 7bf7be29f0c7944f08ae6903a87b04cacc1e0d3e
last_modified_at: 2025-03-02
related_topics:
  - title: español version
    url: /es/common/pre-commit.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/pre-commit.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pre-commit

Create Git hooks that get run before a commit.
More information: <https://pre-commit.com>.

- Install pre-commit into your Git hooks:

`pre-commit install`

- Run pre-commit hooks on all staged files:

`pre-commit run`

- Run pre-commit hooks on all files, staged or unstaged:

`pre-commit run --all-files`

- Clean pre-commit cache:

`pre-commit clean`

- Update pre-commit config file to the latest repos' versions:

`pre-commit autoupdate`
