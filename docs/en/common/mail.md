---
layout: page
title: common/mail (English)
description: "The command operates on the user's mailbox if no argument is given."
content_hash: 82baa0095ef584d47e857d8fb3b6e918b7fc84de
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# mail

The command operates on the user's mailbox if no argument is given.
To send an email the message body is built from `stdin`.
More information: <https://manned.org/mail>.

- Send a typed email message. The command-line below continues after pressing Enter key. Input CC email-id (optional) press Enter key. Input message text (can be multiline). Press Ctrl-D key to complete the message text:

`mail --subject="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">subject line</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">to_user@example.com</span>

- Send an email that contains file content:

`mail --subject="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">$HOSTNAME filename.txt</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">to_user@example.com</span>` < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/filename.txt</span>

- Send a `tar.gz` file as an attachment:

`tar cvzf - `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory1 path/to/directory2</span>` | uuencode `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">data.tar.gz</span>` | mail --subject="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">subject_line</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">to_user@example.com</span>
