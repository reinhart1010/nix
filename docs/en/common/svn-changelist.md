---
layout: page
title: common/svn-changelist (English)
description: "Associate a changelist with a set of files."
content_hash: 35b3ee68f8cc0187aa490e2d4f2ac5410d25b173
last_modified_at: 2024-10-12
tldri18n_status: 2
---
# svn changelist

Associate a changelist with a set of files.
More information: <https://svnbook.red-bean.com/en/1.7/svn.advanced.changelists.html>.

- Add files to a changelist, creating the changelist if it does not exist:

`svn changelist `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">changelist_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file2</span>

- Remove files from a changelist:

`svn changelist --remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file2</span>

- Remove the whole changelist at once:

`svn changelist --remove --recursive --changelist `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">changelist_name</span>` .`

- Add the contents of a space-separated list of directories to a changelist:

`svn changelist --recursive `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">changelist_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory1 path/to/directory2 ...</span>

- Commit a changelist:

`svn commit --changelist `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">changelist_name</span>
