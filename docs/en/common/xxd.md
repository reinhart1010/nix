---
layout: page
title: common/xxd (English)
description: "Create a hexadecimal representation (hexdump) from a binary file, or vice-versa."
content_hash: 11307f855ec9d473ae9bd5c287afca09535d19b9
related_topics:
  - title: italiano version
    url: /it/common/xxd.html
    icon: bi bi-globe
---
# xxd

Create a hexadecimal representation (hexdump) from a binary file, or vice-versa.
More information: <https://manned.org/xxd>.

- Generate a hexdump from a binary file and display the output:

`xxd `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">input_file</span>

- Generate a hexdump from a binary file and save it as a text file:

`xxd `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">input_file</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">output_file</span>

- Display a more compact output, replacing consecutive zeros (if any) with a star:

`xxd -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">input_file</span>

- Display the output with 10 columns of one octet (byte) each:

`xxd -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">input_file</span>

- Display output only up to a length of 32 bytes:

`xxd -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">32</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">input_file</span>

- Display the output in plain mode, without any gaps between the columns:

`xxd -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">input_file</span>

- Revert a plaintext hexdump back into binary, and save it as a binary file:

`xxd -r -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">input_file</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">output_file</span>
