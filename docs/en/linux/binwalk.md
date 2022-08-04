---
layout: page
title: linux/binwalk (English)
description: "Firmware Analysis Tool."
content_hash: 71a8b8f340a300c43de5e356e028d078f1a3267c
related_topics:
  - title: italiano version
    url: /it/linux/binwalk.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/binwalk.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/binwalk.html
    icon: bi bi-globe
---
# binwalk

Firmware Analysis Tool.
More information: <https://github.com/ReFirmLabs/binwalk>.

- Scan a binary file:

`binwalk `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/binary</span>

- Extract files from a binary, specifying the output directory:

`binwalk --extract --directory `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">output_directory</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/binary</span>

- Recursively extract files from a binary limiting the recursion depth to 2:

`binwalk --extract --matryoshka --depth `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/binary</span>

- Extract files from a binary with the specified file signature:

`binwalk --dd '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">png image:png</span>`' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/binary</span>

- Analyze the entropy of a binary, saving the plot with the same name as the binary and `.png` extension appended:

`binwalk --entropy --save `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/binary</span>

- Combine entropy, signature and opcodes analysis in a single command:

`binwalk --entropy --signature --opcodes `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/binary</span>
