---
layout: page
title: common/git-annex (English)
description: "Manage files with Git, without checking their contents in."
content_hash: 63e407dda38f0c2db8dbf38b6f469c8be10152dc
last_modified_at: 2023-08-09
related_topics:
  - title: français version
    url: /fr/common/git-annex.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/git-annex.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-annex.html
    icon: bi bi-globe
---
# git annex

Manage files with Git, without checking their contents in.
When a file is annexed, its content is moved into a key-value store, and a symlink is made that points to the content.
More information: <https://git-annex.branchable.com>.

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

- Display help:

`git annex help`
