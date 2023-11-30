---
layout: page
title: linux/exiqgrep (English)
description: "The `exiqgrep` utility is a Perl script offering possibilities to `grep` in the Exim queue output."
content_hash: d57d42b053b230e6e6cfba10fe6da2ac86c53f46
last_modified_at: 2023-11-30
tldri18n_status: 2
---
# exiqgrep

The `exiqgrep` utility is a Perl script offering possibilities to `grep` in the Exim queue output.
More information: <https://www.exim.org/exim-html-current/doc/html/spec_html/ch-exim_utilities.html>.

- Match the sender address using a case-insensitive search:

`exiqgrep -f '<`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">email@somedomain.com</span>`>'`

- Match the sender address, and display message IDs only:

`exiqgrep -i -f '<`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">email@somedomain.com</span>`>'`

- Match the recipient address:

`exiqgrep -r '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">email@somedomain.com</span>`'`

- Remove all messages matching the sender address from the queue:

`exiqgrep -i -f '<`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">email@somedomain.com</span>`>' | xargs exim -Mrm`

- Test for bounced messages:

`exiqgrep -f '^<>$'`

- Display the count of bounced messages:

`exiqgrep -c -f '^<>$'`
