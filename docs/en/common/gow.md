---
layout: page
title: common/gow (English)
description: "Watches Go files and restarts the app on changes."
content_hash: 8719275acdd09fd0636c33dcca64489aceb0a600
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# gow

Watches Go files and restarts the app on changes.
More information: <https://github.com/mitranim/gow>.

- Start and watch the current directory:

`gow run .`

- Start the application with the specified arguments:

`gow run . `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">argument1 argument2 ...</span>

- Watch subdirectories in verbose mode:

`gow -v -w=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory1,path/to/directory2,...</span>` run .`

- Watch the specified file extensions:

`gow -e=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">go,html</span>` run .`

- Display help:

`gow -h`
