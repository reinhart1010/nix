---
layout: page
title: common/git-cliff (English)
description: "A highly customizable changelog generator."
content_hash: f3cc2b566c507b0fa015913b5235d742b575df4e
last_modified_at: 2025-03-02
related_topics:
  - title: español version
    url: /es/common/git-cliff.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git cliff

A highly customizable changelog generator.
More information: <https://git-cliff.org/docs/usage/args>.

- Generate a changelog from all commits in a Git repository and save it to `CHANGELOG.md`:

`git cliff > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">CHANGELOG.md</span>

- Generate a changelog from commits starting from the latest tag and print it to `stdout`:

`git cliff `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-l|--latest</span>

- Generate a changelog from commits that belong to the current tag (use `git checkout` on a tag before this):

`git cliff --current`

- Generate a changelog from commits that do not belong to a tag:

`git cliff `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-u|--unreleased</span>

- Write the default config file to `cliff.toml` in the current directory:

`git cliff `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-i|--init</span>
