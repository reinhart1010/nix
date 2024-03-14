---
layout: page
title: linux/tftp (English)
description: "Trivial File Transfer Protocol client."
content_hash: fc1b2a969a80da874bdfb1a93046a47e0c7885d1
last_modified_at: 2024-03-14
tldri18n_status: 2
---
# tftp

Trivial File Transfer Protocol client.
More information: <https://manned.org/tftp.1>.

- Connect to a TFTP server specifying its IP address and port:

`tftp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">server_ip</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">port</span>

- Connect to a TFTP server and execute a TFTP [c]ommand:

`tftp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">server_ip</span>` -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>

- Connect to a TFTP server using IPv6 and force originating port to be in [R]ange:

`tftp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">server_ip</span>` -6 -R `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">port</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">port</span>

- Set the transfer mode to binary or ASCIi through the tftp client:

`mode `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">binary|ascii</span>

- Download file from a server through the tftp client:

`get `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file</span>

- Upload file to a server through the tftp client:

`put `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file</span>

- Exit the tftp client:

`quit`
