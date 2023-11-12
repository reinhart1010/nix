---
layout: page
title: common/git-release (English)
description: "Create a Git tag for a release."
content_hash: 0078db6a848d7e56de3ca179eacb21b59f5fd7f7
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# git release

Create a Git tag for a release.
Part of `git-extras`.
More information: <https://github.com/tj/git-extras/blob/master/Commands.md#git-release>.

- Create and push a release:

`git release `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tag_name</span>

- Create and push a signed release:

`git release `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tag_name</span>` -s`

- Create and push a release with a message:

`git release `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">{tag_name}</span>` -m "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">message</span>`"`
