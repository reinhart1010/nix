---
layout: page
title: common/shellcheck (English)
description: "Shell script static analysis tool."
content_hash: 40790a20ad86cc332310fd8c9ed03c181f815112
---
# shellcheck

Shell script static analysis tool.
Check shell scripts for errors, usage of deprecated/insecure features, and bad practices.
More information: <https://www.shellcheck.net>.

- Check a shell script:

`shellcheck `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/script.sh</span>

- Check a shell script interpreting it as the specified shell dialect (overrides the shebang at the top of the script):

`shellcheck --shell `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sh|bash|dash|ksh</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/script.sh</span>

- Ignore one or more error types:

`shellcheck --exclude `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">SC1009,SC1073</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/script.sh</span>

- Also check any sourced shell scripts:

`shellcheck --checked-sourced `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/script.sh</span>

- Display output in the specified format (defaults to `tty`):

`shellcheck --format `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tty|checkstyle|diff|gcc|json|json1|quiet</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/script.sh</span>

- Enable one or more optional checks:

`shellcheck --enable=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">add-default-case|avoid-nullary-conditions</span>

- List all available optional checks that are disabled by default:

`shellcheck --list-optional`
