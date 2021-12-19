---
layout: page
title: linux/reportbug (English)
description: "Bug report tool of Debian distribution."
content_hash: ce3fcb051c5ed2fccb0c8ef42d302043cf1ed1e5
---
# reportbug

Bug report tool of Debian distribution.
More information: <https://manpages.debian.org/buster/reportbug/reportbug.1.en.html>.

- Generate a bug report about a specific package, then send it by e-mail:

`reportbug `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- Report a bug that is not about a specific package (general problem, infrastructure, etc.):

`reportbug other`

- Write the bug report to a file instead of sending it by e-mail:

`reportbug -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filename</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>
