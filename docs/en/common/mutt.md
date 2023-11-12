---
layout: page
title: common/mutt (English)
description: "Command-line email client."
content_hash: ef6c020f4ce817122fa54a47f1696caa6ccbe05f
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# mutt

Command-line email client.
More information: <http://mutt.org>.

- Open the specified mailbox:

`mutt -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mailbox</span>

- Send an email and specify a subject and a cc recipient:

`mutt -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">subject</span>` -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cc@example.com</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">recipient@example.com</span>

- Send an email with files attached:

`mutt -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file2</span>` -- `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">recipient@example.com</span>

- Specify a file to include as the message body:

`mutt -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">recipient@example.com</span>

- Specify a draft file containing the header and the body of the message, in RFC 5322 format:

`mutt -H `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">recipient@example.com</span>
