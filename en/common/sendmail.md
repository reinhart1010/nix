---
layout: page
title: common/sendmail (English)
description: "Send email from the command-line."
content_hash: 9244f2f0b03b158d0ad70eff22b06e2413cf0332
---
# sendmail

Send email from the command-line.
More information: <https://manned.org/sendmail>.

- Send a message with the content of `message.txt` to the mail directory of local user `username`:

`sendmail `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>` < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">message.txt</span>

- Send an email from you@yourdomain.com (assuming the mail server is configured for this) to test@gmail.com containing the message in `message.txt`:

`sendmail -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">you@yourdomain.com</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">test@gmail.com</span>` < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">message.txt</span>

- Send an email from you@yourdomain.com (assuming the mail server is configured for this) to test@gmail.com containing the file `file.zip`:

`sendmail -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">you@yourdomain.com</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">test@gmail.com</span>` < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file.zip</span>
