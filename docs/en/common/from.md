---
layout: page
title: common/from (English)
description: "Prints mail header lines from the current user's mailbox."
content_hash: a0ecf77e9f08a449ca5fa7379c78210650d6af41
---
# from

Prints mail header lines from the current user's mailbox.
More information: <https://mailutils.org/manual/html_chapter/Programs.html#frm-and-from>.

- List mail:

`from`

- Display the number of messages stored:

`from --count`

- List mail in the specified mailbox directory:

`MAIL=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/mailbox</span>` from`

- Print the mail from the specified address:

`from --sender=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">me@example.com</span>
