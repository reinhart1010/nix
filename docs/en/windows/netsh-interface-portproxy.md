---
layout: page
title: windows/netsh-interface-portproxy (English)
description: "Configure and display the status of various network components."
content_hash: ab13fe50892b26c3053777df0fa4132c89eaba25
last_modified_at: 2023-07-14
---
# netsh interface portproxy

Configure and display the status of various network components.
More information: <https://learn.microsoft.com/en-us/windows-server/networking/technologies/netsh/netsh-interface-portproxy>.

- Display the current port forwarding setup:

`netsh interface portproxy show all`

- Set up IPv4 port forwarding (run in elevated console):

`netsh interface portproxy add v4tov4 listenaddress=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">192.168.0.1</span>` listenport=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">8080</span>`  connectaddress=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10.0.0.1</span>` connectport=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">80</span>

- Remove IPv4 port forwarding (run in elevated console):

`netsh interface portproxy delete v4tov4 listenaddress=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">192.168.0.1</span>` listenport=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">8080</span>

- Display help:

`netsh interface portproxy`
