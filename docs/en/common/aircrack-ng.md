---
layout: page
title: common/aircrack-ng (English)
description: "Crack WEP and WPA/WPA2 keys from handshake in captured packets."
content_hash: ef4f67d2786fe69e1045f62c7f380788e93dee5d
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/aircrack-ng.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/aircrack-ng.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/aircrack-ng.html
    icon: bi bi-globe
tldri18n_status: 2
---
# aircrack-ng

Crack WEP and WPA/WPA2 keys from handshake in captured packets.
Part of Aircrack-ng network software suite.
More information: <https://www.aircrack-ng.org/doku.php?id=aircrack-ng>.

- Crack key from capture file using [w]ordlist:

`aircrack-ng -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/wordlist.txt</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/capture.cap</span>

- Crack key from capture file using [w]ordlist and the access point's [e]ssid:

`aircrack-ng -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/wordlist.txt</span>` -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">essid</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/capture.cap</span>

- Crack key from capture file using [w]ordlist and the access point's MAC address:

`aircrack-ng -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/wordlist.txt</span>` --bssid `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mac</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/capture.cap</span>
