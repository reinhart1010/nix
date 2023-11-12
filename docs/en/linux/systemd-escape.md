---
layout: page
title: linux/systemd-escape (English)
description: "Escape strings for usage in systemd unit names."
content_hash: 843e8838ddeead9b5afdf933ae06fc3c60da2d26
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# systemd-escape

Escape strings for usage in systemd unit names.
More information: <https://www.freedesktop.org/software/systemd/man/systemd-escape.html>.

- Escape the given text:

`systemd-escape `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">text</span>

- Reverse the escaping process:

`systemd-escape --unescape `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">text</span>

- Treat the given text as a path:

`systemd-escape --path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">text</span>

- Append the given suffix to the escaped text:

`systemd-escape --suffix `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">suffix</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">text</span>

- Use a template and inject the escaped text:

`systemd-escape --template `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">template</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">text</span>
