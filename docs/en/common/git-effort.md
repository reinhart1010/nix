---
layout: page
title: common/git-effort (English)
description: "Display how much activity a file has had, showing commits per file and \"active days\" i.e. total number of days that contributed to the file."
content_hash: 333c15e7c8daa5e0d8afa32dfc063fd335e7b77c
---
# git effort

Display how much activity a file has had, showing commits per file and "active days" i.e. total number of days that contributed to the file.
Part of `git-extras`.
More information: <https://github.com/tj/git-extras/blob/master/Commands.md#git-effort>.

- Display each file in the repository, showing commits and active days:

`git effort`

- Display files modified by a specific number of commits or more, showing commits and active days:

`git effort --above `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5</span>

- Display files modified by a specific author, showing commits and active days:

`git effort -- --author="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>`"`

- Display files modified since a specific time/date, showing commits and active days:

`git effort -- --since="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">last month</span>`"`

- Display only the specified files or directories, showing commits and active days:

`git effort `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file_or_directory1 path/to/file_or_directory2 ...</span>

- Display all files in a specific directory, showing commits and active days:

`git effort `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory/*</span>
