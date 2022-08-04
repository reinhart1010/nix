---
layout: page
title: linux/tshark (English)
description: "Packet analysis tool, CLI version of Wireshark."
content_hash: 696a3917a54748b1a0501715dd17a18c14f684ef
---
# tshark

Packet analysis tool, CLI version of Wireshark.
More information: <https://tshark.dev/>.

- Monitor everything on localhost:

`tshark`

- Only capture packets matching a specific capture filter:

`tshark -f '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">udp port 53</span>`'`

- Only show packets matching a specific output filter:

`tshark -Y '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http.request.method == "GET"</span>`'`

- Decode a TCP port using a specific protocol (e.g. HTTP):

`tshark -d tcp.port==`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">8888</span>`,`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http</span>

- Specify the format of captured output:

`tshark -T `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">json|text|ps|…</span>

- Select specific fields to output:

`tshark -T `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">fields|ek|json|pdml</span>` -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http.request.method</span>` -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip.src</span>

- Write captured packet to a file:

`tshark -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Analyze packets from a file:

`tshark -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filename</span>`.pcap`
