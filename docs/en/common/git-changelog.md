---
layout: page
title: common/git-changelog (English)
description: "Generate a changelog report from repository commits and tags."
content_hash: 0b4b4acac0b6aeb7c2ec6457ad041d65db061afc
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# git changelog

Generate a changelog report from repository commits and tags.
Part of `git-extras`.
More information: <https://github.com/tj/git-extras/blob/master/Commands.md#git-changelog>.

- Update existing file or create a new `History.md` file with the commit messages since the latest Git tag:

`git changelog`

- List commits from the current version:

`git changelog --list`

- List a range of commits from the tag named `2.1.0` to now:

`git changelog --list --start-tag `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2.1.0</span>

- List pretty formatted range of commits between the tag `0.5.0` and the tag `1.0.0`:

`git changelog --start-tag `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0.5.0</span>` --final-tag `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1.0.0</span>

- List pretty formatted range of commits between the commit `0b97430` and the tag `1.0.0`:

`git changelog --start-commit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0b97430</span>` --final-tag `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1.0.0</span>

- Specify `CHANGELOG.md` as the output file:

`git changelog `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">CHANGELOG.md</span>

- Replace contents of current changelog file entirely:

`git changelog --prune-old`
