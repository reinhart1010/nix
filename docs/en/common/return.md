---
layout: page
title: common/return (English)
description: "Exit a function or a script if run with `source`."
content_hash: f4f6c0779f6337d3a20179928867ea7e68db2699
last_modified_at: 2024-12-27
tldri18n_status: 2
---
# return

Exit a function or a script if run with `source`.
More information: <https://www.gnu.org/software/bash/manual/bash.html#index-return>.

- Exit a function prematurely:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">func_name</span>`() { `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">echo "This is reached"</span>`; return; `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">echo "This is not"</span>`; }`

- Specify the function's return value:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">func_name</span>`() { return `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">N</span>`; }`
