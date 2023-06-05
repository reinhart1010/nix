---
layout: page
title: common/gitwatch (English)
description: "Automatically commit file or directory changes to a git repository."
content_hash: 1a7be43e7a0bb5e40af1de4c7b9c20f6f6751d0d
last_modified_at: 2023-06-05
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># gitwatch

Automatically commit file or directory changes to a git repository.
More information: <https://github.com/gitwatch/gitwatch>.

- Automatically commit any changes made to a file or directory:

`gitwatch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file_or_directory</span>

- Automatically commit changes and push them to a remote repository:

`gitwatch -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">remote_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file_or_directory</span>

- Automatically commit changes and push them to a specific branch of a remote repository:

`gitwatch -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">remote_name</span>` -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">branch_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file_or_directory</span>
