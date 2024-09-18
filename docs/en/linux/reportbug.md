---
layout: page
title: linux/reportbug (English)
description: "Bug report tool of Debian distribution."
content_hash: ec797700666d81aac3ffcc04eea4fcedb8ceaa88
last_modified_at: 2024-09-18
tldri18n_status: 2
---
# reportbug

Bug report tool of Debian distribution.
More information: <https://manned.org/reportbug>.

- Generate a bug report about a specific package, then send it by e-mail:

`reportbug `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- Report a bug that is not about a specific package (general problem, infrastructure, etc.):

`reportbug other`

- Write the bug report to a file instead of sending it by e-mail:

`reportbug -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filename</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>
