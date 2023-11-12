---
layout: page
title: linux/reportbug (English)
description: "Bug report tool of Debian distribution."
content_hash: 7886fcbe943f5c24813b72df837b50bd0c6ce545
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# reportbug

Bug report tool of Debian distribution.
More information: <https://manpages.debian.org/latest/reportbug/reportbug.html>.

- Generate a bug report about a specific package, then send it by e-mail:

`reportbug `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- Report a bug that is not about a specific package (general problem, infrastructure, etc.):

`reportbug other`

- Write the bug report to a file instead of sending it by e-mail:

`reportbug -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filename</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>
