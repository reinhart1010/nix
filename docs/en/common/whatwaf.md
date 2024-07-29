---
layout: page
title: common/whatwaf (English)
description: "Detect and bypass web application firewalls and protection systems."
content_hash: ffa5b8e3dbc869533b0a7555d976fcf2ce94d24c
last_modified_at: 2024-07-29
tldri18n_status: 2
---
# whatwaf

Detect and bypass web application firewalls and protection systems.
More information: <https://github.com/Ekultek/WhatWaf>.

- Detect protection on a single [u]RL, optionally use verbose output:

`whatwaf --url `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com</span>` --verbose`

- Detect protection on a [l]ist of URLs in parallel from a file (one URL per line):

`whatwaf --threads `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">number</span>` --list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Send requests through a proxy and use custom payload list from a file (one payload per line):

`whatwaf --proxy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://127.0.0.1:8080</span>` --pl `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>` -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com</span>

- Send requests through Tor (Tor must be installed) using custom [p]ayloads (comma-separated):

`whatwaf --tor --payloads '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">payload1,payload2,...</span>`' -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com</span>

- Use a random user-agent, set throttling and timeout, send a [P]OST request, and force HTTPS connection:

`whatwaf --ra --throttle `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">seconds</span>` --timeout `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">seconds</span>` --post --force-ssl -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://example.com</span>

- List all WAFs that can be detected:

`whatwaf --wafs`

- List all available tamper scripts:

`whatwaf --tampers`
