---
layout: page
title: common/webstorm (English)
description: "The JetBrains JavaScript IDE."
content_hash: 92a3801cfa21b74dcb7b4123bd6e8263eb14691c
last_modified_at: 2024-01-31
tldri18n_status: 2
---
# webstorm

The JetBrains JavaScript IDE.
More information: <https://www.jetbrains.com/help/webstorm/working-with-the-ide-features-from-command-line.html>.

- Open the current directory in WebStorm:

`webstorm`

- Open a specific directory in WebStorm:

`webstorm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Open specific files in the LightEdit mode﻿:

`webstorm -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1 path/to/file2 ...</span>

- Open and wait until done editing a specific file in the LightEdit mode:

`webstorm --wait -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Open a file with the cursor at the specific line:

`webstorm --line `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">line_number</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Open and compare files (supports up to 3 files):

`webstorm diff `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1 path/to/file2 path/to/optional_file3</span>

- Open and perform a three-way merge:

`webstorm merge `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/left_file</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/right_file</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/target_file</span>
