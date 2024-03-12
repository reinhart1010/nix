---
layout: page
title: common/shellcheck (English)
description: "Statically check shell scripts for errors, usage of deprecated/insecure features, and bad practices."
content_hash: a9e0aa1d2044fb53e1165e9ea00ae89102b62645
last_modified_at: 2024-03-12
tldri18n_status: 2
---
# shellcheck

Statically check shell scripts for errors, usage of deprecated/insecure features, and bad practices.
More information: <https://github.com/koalaman/shellcheck/wiki>.

- Check a shell script:

`shellcheck `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/script.sh</span>

- Check a shell script interpreting it as the specified [s]hell dialect (overrides the shebang at the top of the script):

`shellcheck --shell `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sh|bash|dash|ksh</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/script.sh</span>

- Ignor[e] one or more error types:

`shellcheck --exclude `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">SC1009,SC1073,...</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/script.sh</span>

- Also check any sourced shell scripts:

`shellcheck --check-sourced `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/script.sh</span>

- Display output in the specified [f]ormat (defaults to `tty`):

`shellcheck --format `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tty|checkstyle|diff|gcc|json|json1|quiet</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/script.sh</span>

- Enable one or more [o]ptional checks:

`shellcheck --enable `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">add-default-case,avoid-nullary-conditions,...</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/script.sh</span>

- List all available optional checks that are disabled by default:

`shellcheck --list-optional`

- Adjust the level of [S]everity to consider (defaults to `style`):

`shellcheck --severity `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">error|warning|info|style</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/script.sh</span>
