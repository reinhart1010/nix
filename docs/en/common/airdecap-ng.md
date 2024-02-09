---
layout: page
title: common/airdecap-ng (English)
description: "Decrypt a WEP, WPA, or WPA2 encrypted capture file."
content_hash: 5103fae40c544aaccc30cf3dc701e077e522817d
last_modified_at: 2024-02-09
related_topics:
  - title: Indonesia version
    url: /id/common/airdecap-ng.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/airdecap-ng.html
    icon: bi bi-globe
tldri18n_status: 2
---
# airdecap-ng

Decrypt a WEP, WPA, or WPA2 encrypted capture file.
Part of Aircrack-ng network software suite.
More information: <https://www.aircrack-ng.org/doku.php?id=airdecap-ng>.

- Remove wireless headers from an open network capture file and use the access point's MAC address to filter:

`airdecap-ng -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ap_mac</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/capture.cap</span>

- Decrypt a [w]EP encrypted capture file using the key in hex format:

`airdecap-ng -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hex_key</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/capture.cap</span>

- Decrypt a WPA/WPA2 encrypted capture file using the access point's [e]ssid and [p]assword:

`airdecap-ng -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">essid</span>` -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">password</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/capture.cap</span>

- Decrypt a WPA/WPA2 encrypted capture file preserving the headers using the access point's [e]ssid and [p]assword:

`airdecap-ng -l -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">essid</span>` -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">password</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/capture.cap</span>

- Decrypt a WPA/WPA2 encrypted capture file using the access point's [e]ssid and [p]assword and use its MAC address to filter:

`airdecap-ng -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ap_mac</span>` -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">essid</span>` -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">password</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/capture.cap</span>
