---
layout: page
title: common/from (English)
description: "Print mail header lines from the current user's mailbox."
content_hash: de5754d809553c43412ff02abf8a94e2bf9f6631
last_modified_at: 2024-04-18
tldri18n_status: 2
---
# from

Print mail header lines from the current user's mailbox.
More information: <https://mailutils.org/manual/html_chapter/Programs.html#frm-and-from>.

- List mail:

`from`

- Display the number of messages stored:

`from --count`

- List mail in the specified mailbox directory:

`MAIL=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/mailbox</span>` from`

- Print the mail from the specified address:

`from --sender=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">me@example.com</span>
