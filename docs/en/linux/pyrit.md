---
layout: page
title: linux/pyrit (English)
description: "WPA/WPA2 cracking tool using computational power."
content_hash: 1123573d6572e77e89f32108291c8640a3676d6e
last_modified_at: 2022-12-30
---
# pyrit

WPA/WPA2 cracking tool using computational power.
More information: <https://github.com/JPaulMora/Pyrit>.

- Display system cracking speed:

`pyrit benchmark`

- List available cores:

`pyrit list_cores`

- Set [e]SSID:

`pyrit -e "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ESSID</span>`" create_essid`

- [r]ead and analyze a specific packet capture file:

`pyrit -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.cap|path/to/file.pcap</span>` analyze`

- Read and [i]mport passwords to the current database:

`pyrit -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">import_unique_passwords|unique_passwords|import_passwords</span>

- Exp[o]rt passwords from database to a specific file:

`pyrit -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>` export_passwords`

- Translate passwords with Pired Master Keys:

`pyrit batch`

- [r]ead the capture file and crack the password:

`pyrit -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>` attack_db`
