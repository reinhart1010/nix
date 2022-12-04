---
layout: page
title: common/unexpand (English)
description: "Convert spaces to tabs."
content_hash: 1f164447be49dec5c8ab03a1ae9ddfb7bca2f246
last_modified_at: 2022-12-04
---
# unexpand

Convert spaces to tabs.
More information: <https://www.gnu.org/software/coreutils/unexpand>.

- Convert blanks in each file to tabs, writing to standard output:

`unexpand `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Convert blanks to tabs, reading from standard output:

`unexpand`

- Convert all blanks, instead of just initial blanks:

`unexpand -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Convert only leading sequences of blanks (overrides -a):

`unexpand --first-only `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Have tabs a certain number of characters apart, not 8 (enables -a):

`unexpand -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">number</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>
