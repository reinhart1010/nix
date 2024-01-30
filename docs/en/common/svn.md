---
layout: page
title: common/svn (English)
description: "Subversion command-line client tool."
content_hash: 6cee553d69071dc0a1b27ed1eb0745f628ef7406
last_modified_at: 2024-01-30
tldri18n_status: 2
---
# svn

Subversion command-line client tool.
More information: <https://subversion.apache.org>.

- Check out a working copy from a repository:

`svn co `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url/to/repository</span>

- Bring changes from the repository into the working copy:

`svn up`

- Put files and directories under version control, scheduling them for addition to repository. They will be added in next commit:

`svn add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">PATH</span>

- Send changes from your working copy to the repository:

`svn ci -m `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commit_log_message</span>` [`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">PATH</span>`]`

- Display changes from the last 10 revisions, showing modified files for each revision:

`svn log -vl `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>

- Display help:

`svn help`
