---
layout: page
title: common/gitlint (English)
description: "Git commit message linter checks your commit messages for style."
content_hash: 788bbbbe78b7cd4e9713ebee925fee168ebdd8fb
last_modified_at: 2023-05-02
---
# gitlint

Git commit message linter checks your commit messages for style.
More information: <https://jorisroovers.com/gitlint/>.

- Check the last commit message:

`gitlint`

- The range of commits to lint:

`gitlint --commits `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">single_refspec_argument</span>

- Path to a directory or Python module with extra user-defined rules:

`gitlint --extra-path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Start a specific CI job:

`gitlint --target `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/target_directory</span>

- Path to a file containing a commit-msg:

`gitlint --msg-filename `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/filename</span>

- Read staged commit meta-info from the local repository:

`gitlint --staged`
