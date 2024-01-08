---
layout: page
title: linux/export (English)
description: "Export shell variables to child processes."
content_hash: 5633537eec37fc80a4f02df14a790652c1fd12d2
last_modified_at: 2024-01-08
tldri18n_status: 2
---
# export

Export shell variables to child processes.
More information: <https://www.gnu.org/software/bash/manual/bash.html#index-export>.

- Set an environment variable:

`export `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">VARIABLE</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">value</span>

- Unset an environment variable:

`export -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">VARIABLE</span>

- Export a function to child processes:

`export -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">FUNCTION_NAME</span>

- Append a pathname to the environment variable `PATH`:

`export PATH=$PATH:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/append</span>
