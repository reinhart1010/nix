---
layout: page
title: common/dvc-add (English)
description: "Add changed files to the index."
content_hash: ef4794e4df19e904506275c910db1cb92dd49f75
---
# dvc add

Add changed files to the index.
More information: <https://dvc.org/doc/command-reference/add>.

- Add a single target file to the index:

`dvc add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Add a target directory to the index:

`dvc add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Recursively add all the files in a given target directory:

`dvc add --recursive `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Add a target file with a custom `.dvc` filename:

`dvc add --file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">custom_name.dvc</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>
