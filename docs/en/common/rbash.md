---
layout: page
title: common/rbash (English)
description: "Restricted Bash shell, equivalent to `bash --restricted`."
content_hash: 1ec06b4b7801f3e9c202c878f137ea0e90b72b08
last_modified_at: 2022-12-04
---
# rbash

Restricted Bash shell, equivalent to `bash --restricted`.
Does not permit changing the working directory, redirecting command output, or modifying environment variables, among other things.
See also `histexpand` for history expansion.
More information: <https://www.gnu.org/software/bash/manual/html_node/The-Restricted-Shell>.

- Start an interactive shell session:

`rbash`

- Execute a command and then exit:

`rbash -c "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>`"`

- Execute a script:

`rbash `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/script.sh</span>

- Execute a script, printing each command before executing it:

`rbash -x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/script.sh</span>

- Execute commands from a script, stopping at the first error:

`rbash -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/script.sh</span>

- Read and execute commands from `stdin`:

`rbash -s`
