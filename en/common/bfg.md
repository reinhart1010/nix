---
layout: page
title: common/bfg (English)
description: "Remove large files or passwords from Git history like git-filter-branch."
content_hash: 5f7b05630ec9571dcf466bbc1e077edbf03e243b
---
# bfg

Remove large files or passwords from Git history like git-filter-branch.
Note: if your repository is connected to a remote, you will need to force push to it.
More information: <https://rtyley.github.io/bfg-repo-cleaner/>.

- Remove a file with sensitive data but leave the latest commit untouched:

`bfg --delete-files `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file_with_sensitive_data</span>

- Remove all text mentioned in the specified file wherever it can be found in the repository's history:

`bfg --replace-text `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.txt</span>
