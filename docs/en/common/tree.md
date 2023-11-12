---
layout: page
title: common/tree (English)
description: "Show the contents of the current directory as a tree."
content_hash: 6d4b71d518eaa7abe47bc3c3eabab679045c3dbd
last_modified_at: 2023-11-12
related_topics:
  - title: español version
    url: /es/common/tree.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/tree.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/tree.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/tree.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/tree.html
    icon: bi bi-globe
tldri18n_status: 2
---
# tree

Show the contents of the current directory as a tree.
More information: <http://mama.indstate.edu/users/ice/tree/>.

- Print files and directories up to 'num' levels of depth (where 1 means the current directory):

`tree -L `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">num</span>

- Print directories only:

`tree -d`

- Print hidden files too with colorization on:

`tree -a -C`

- Print the tree without indentation lines, showing the full path instead (use `-N` to not escape non-printable characters):

`tree -i -f`

- Print the size of each file and the cumulative size of each directory, in human-readable format:

`tree -s -h --du`

- Print files within the tree hierarchy, using a wildcard (glob) pattern, and pruning out directories that don't contain matching files:

`tree -P '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.txt</span>`' --prune`

- Print directories within the tree hierarchy, using the wildcard (glob) pattern, and pruning out directories that aren't ancestors of the wanted one:

`tree -P `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">directory_name</span>` --matchdirs --prune`

- Print the tree ignoring the given directories:

`tree -I '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">directory_name1|directory_name2</span>`'`
