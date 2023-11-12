---
layout: page
title: sunos/snoop (English)
description: "Network packet sniffer."
content_hash: 974c9411e200d3c8382e81ef711e438f802b299d
last_modified_at: 2023-11-12
related_topics:
  - title: বাংলা version
    url: /bn/sunos/snoop.html
    icon: bi bi-globe
  - title: français version
    url: /fr/sunos/snoop.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/sunos/snoop.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/sunos/snoop.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/sunos/snoop.html
    icon: bi bi-globe
tldri18n_status: 2
---
# snoop

Network packet sniffer.
SunOS equivalent of tcpdump.
More information: <https://www.unix.com/man-page/sunos/1m/snoop>.

- Capture packets on a specific network interface:

`snoop -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">e1000g0</span>

- Save captured packets in a file instead of displaying them:

`snoop -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Display verbose protocol layer summary of packets from a file:

`snoop -V -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Capture network packets that come from a hostname and go to a given port:

`snoop to port `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">port</span>` from host `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hostname</span>

- Capture and show a hex-dump of network packets exchanged between two IP addresses:

`snoop -x0 -p4 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip2</span>
