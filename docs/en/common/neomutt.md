---
layout: page
title: common/neomutt (English)
description: "NeoMutt command-line email client."
content_hash: 2e540a385a9733ef28d4218bc29bcba24f7639af
last_modified_at: 2023-05-31
---
# neomutt

NeoMutt command-line email client.
More information: <https://neomutt.org>.

- Open the specified mailbox:

`neomutt -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/mailbox</span>

- Start writing an email and specify a subject and a `cc` recipient:

`neomutt -s "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">subject</span>`" -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cc@example.com</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">recipient@example.com</span>

- Send an email with files attached:

`neomutt -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1 path/to/file2 ...</span>` -- `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">recipient@example.com</span>

- Specify a file to include as the message body:

`neomutt -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">recipient@example.com</span>

- Specify a draft file containing the header and the body of the message, in RFC 5322 format:

`neomutt -H `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">recipient@example.com</span>
