---
layout: page
title: common/git-annex (English)
description: "Manage files with Git, without checking their contents in."
content_hash: a41a46d6926f7f2f0c05aff64f822b2da5468494
related_topics:
  - title: français version
    url: /fr/common/git-annex.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/git-annex.html
    icon: bi bi-globe
---
# git annex

Manage files with Git, without checking their contents in.
When a file is annexed, its content is moved into a key-value store, and a symlink is made that points to the content.
More information: <https://git-annex.branchable.com>.

- Help:

`git annex help`

- Initialize a repo with Git annex:

`git annex init`

- Add a file:

`git annex add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file_or_directory</span>

- Show the current status of a file or directory:

`git annex status `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file_or_directory</span>

- Synchronize a local repository with a remote:

`git annex `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">remote</span>

- Get a file or directory:

`git annex get `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file_or_directory</span>
