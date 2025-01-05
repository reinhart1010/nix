---
layout: page
title: common/if (English)
description: "Performs conditional processing in shell scripts."
content_hash: e4f847254526312f75f8e10ca26206cc2edb2a67
last_modified_at: 2025-01-05
related_topics:
  - title: 한국어 version
    url: /ko/common/if.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/if.html
    icon: bi bi-globe
tldri18n_status: 2
---
# if

Performs conditional processing in shell scripts.
See also: `test`, `[`.
More information: <https://www.gnu.org/software/bash/manual/bash.html#Conditional-Constructs>.

- Execute the specified commands if the condition command's exit status is zero:

`if `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">condition_command</span>`; then `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">echo "Condition is true"</span>`; fi`

- Execute the specified commands if the condition command's exit status is not zero:

`if ! `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">condition_command</span>`; then `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">echo "Condition is true"</span>`; fi`

- Execute the first specified commands if the condition command's exit status is zero otherwise execute the second specified commands:

`if `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">condition_command</span>`; then `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">echo "Condition is true"</span>`; else `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">echo "Condition is false"</span>`; fi`

- Check whether a [f]ile exists:

`if [[ -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>` ]]; then `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">echo "Condition is true"</span>`; fi`

- Check whether a [d]irectory exists:

`if [[ -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>` ]]; then `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">echo "Condition is true"</span>`; fi`

- Check whether a file or directory [e]xists:

`if [[ -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file_or_directory</span>` ]]; then `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">echo "Condition is true"</span>`; fi`

- Check whether a variable is defined:

`if [[ -n "$`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">variable</span>`" ]]; then `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">echo "Condition is true"</span>`; fi`

- List all possible conditions (`test` is an alias to `[`; both are commonly used with `if`):

`man test`
