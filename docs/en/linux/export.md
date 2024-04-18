---
layout: page
title: linux/export (English)
description: "Export shell variables to child processes."
content_hash: 55aca4ac084c4996126fd369bdd7b49f50e70aea
last_modified_at: 2024-04-18
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

- Display a list of active exported variables in shell command form:

`export -p`
