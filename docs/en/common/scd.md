---
layout: page
title: common/scd (English)
description: "File manager focused on shell integration."
content_hash: 3654fe4c7bb4b8e7627d928cc2bfb94eb64f58db
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# scd

File manager focused on shell integration.
More information: <https://github.com/cshuaimin/scd>.

- Index paths recursively for the very first run:

`scd -ar `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Change to a specific directory:

`scd `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Change to a path matching specific patterns:

`scd "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pattern1 pattern2 ...</span>`"`

- Show selection menu and ranking of 20 most likely directories:

`scd -v`

- Add a specific alias for the current directory:

`scd --alias=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">word</span>

- Change to a directory using a specific alias:

`scd `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">word</span>
