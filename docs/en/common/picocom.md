---
layout: page
title: common/picocom (English)
description: "Minimal program to emulate serial consoles."
content_hash: e3c2a23bbd6b866ef79d1db94241fa5e4b712074
last_modified_at: 2024-01-20
tldri18n_status: 2
---
# picocom

Minimal program to emulate serial consoles.
More information: <https://manned.org/picocom>.

- Connect to a serial console with a specified baud rate:

`picocom `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/ttyXYZ</span>` --baud `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">baud_rate</span>

- Map special characters (e.g. `LF` to `CRLF`):

`picocom `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/ttyXYZ</span>` --imap `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">lfcrlf</span>
