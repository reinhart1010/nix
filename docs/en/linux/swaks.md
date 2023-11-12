---
layout: page
title: linux/swaks (English)
description: "Swiss Army Knife SMTP, the all-purpose SMTP transaction tester."
content_hash: b6563503a335b396185482f67a52270aea48fa06
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# swaks

Swiss Army Knife SMTP, the all-purpose SMTP transaction tester.
More information: <https://github.com/jetmore/swaks/blob/develop/doc/base.pod>.

- Deliver a standard test email to `user@example.com` on port 25 of `test-server.example.net`:

`swaks --to `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">user@example.com</span>` --server `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">test-server.example.net</span>

- Deliver a standard test email, requiring CRAM-MD5 authentication as user `me@example.com`. An "X-Test" header will be added to the email body:

`swaks --to `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">user@example.com</span>` --from `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">me@example.com</span>` --auth `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">CRAM-MD5</span>` --auth-user `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">me@example.com</span>` --header-X-Test "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">test_email</span>`"`

- Test a virus scanner using EICAR in an attachment. Don't show the message DATA part:

`swaks -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">user@example.com</span>` --attach - --server `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">test-server.example.com</span>` --suppress-data `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/eicar.txt</span>

- Test a spam scanner using GTUBE in the body of an email, routed via the MX records for `example.com`:

`swaks --to `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">user@example.com</span>` --body `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/gtube_file</span>

- Deliver a standard test email to `user@example.com` using the LMTP protocol via a UNIX domain socket file:

`swaks --to `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">user@example.com</span>` --socket `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/var/lda.sock</span>` --protocol `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">LMTP</span>
