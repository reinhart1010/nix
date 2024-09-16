---
layout: page
title: linux/chat (English)
description: "Automate conversations with a modem or serial device."
content_hash: e73c514a22afa5e1b4519d19e1beef66b210995d
last_modified_at: 2024-09-16
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/chat.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># chat

Automate conversations with a modem or serial device.
Commonly used to establish PPP (Point-to-Point Protocol) connections.
More information: <https://manned.org/chat.8>.

- Execute a chat script directly from the command line:

`chat '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">expect_send_pairs</span>`'`

- Execute a chat script from a file:

`chat -f '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/chat_script</span>`'`

- Set a custom timeout (in seconds) for expecting a response:

`chat -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">timeout_in_seconds</span>` '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">expect_send_pairs</span>`'`

- Enable verbose output to log the conversation to `syslog`:

`chat -v '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">expect_send_pairs</span>`'`

- Use a report file to log specific strings received during the conversation:

`chat -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/report_file</span>` '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">expect_send_pairs</span>`'`

- Dial a phone number using a variable, substituting `\T` in the script:

`chat -T '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">phone_number</span>`' '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">"ATDT\\T CONNECT"</span>`'`

- Include an abort condition if a specific string is received:

`chat 'ABORT "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">error_string</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">expect_send_pairs</span>`'`
