---
layout: page
title: common/mail (English)
description: "The command operates on the user's mailbox if no argument is given."
content_hash: 57ea3bf89c2243e56cc439d6c0daa0353b16eaec
last_modified_at: 2024-10-16
tldri18n_status: 2
---
# mail

The command operates on the user's mailbox if no argument is given.
To send an email the message body is built from `stdin`.
More information: <https://manned.org/mail>.

- Open an interactive prompt to check personal mail:

`mail`

- Send a typed email message with optional CC. The command-line below continues after pressing `<Enter>`. Input message text (can be multiline). Press `<Ctrl>-D` to complete the message text:

`mail --subject="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">subject line</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">to_user@example.com</span>` --cc="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cc_email_address</span>`"`

- Send an email that contains file content:

`mail --subject="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">$HOSTNAME filename.txt</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">to_user@example.com</span>` < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/filename.txt</span>

- Send a `tar.gz` file as an attachment:

`tar cvzf - `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory1 path/to/directory2</span>` | uuencode `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">data.tar.gz</span>` | mail --subject="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">subject_line</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">to_user@example.com</span>
