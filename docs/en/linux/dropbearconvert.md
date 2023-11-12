---
layout: page
title: linux/dropbearconvert (English)
description: "Convert between Dropbear and OpenSSH private key formats."
content_hash: 2f1b01e40c74f54766bcfa98862fcaaef489ab6f
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# dropbearconvert

Convert between Dropbear and OpenSSH private key formats.
More information: <https://manned.org/dropbearconvert.1>.

- Convert an OpenSSH private key to the Dropbear format:

`dropbearconvert openssh dropbear `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input_key</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output_key</span>

- Convert a Dropbear private key to the OpenSSH format:

`dropbearconvert dropbear openssh `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input_key</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output_key</span>
