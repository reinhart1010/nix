---
layout: page
title: common/gitwatch (English)
description: "Automatically commit file or directory changes to a Git repository."
content_hash: 82a008891747a8fe72beb86b19dddf80c9dadadc
last_modified_at: 2024-01-30
tldri18n_status: 2
---
# gitwatch

Automatically commit file or directory changes to a Git repository.
More information: <https://github.com/gitwatch/gitwatch>.

- Automatically commit any changes made to a file or directory:

`gitwatch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file_or_directory</span>

- Automatically commit changes and push them to a remote repository:

`gitwatch -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">remote_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file_or_directory</span>

- Automatically commit changes and push them to a specific branch of a remote repository:

`gitwatch -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">remote_name</span>` -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">branch_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file_or_directory</span>
