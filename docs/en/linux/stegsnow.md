---
layout: page
title: linux/stegsnow (English)
description: "Steganography tool for concealing and extracting messages in text files encoded as tabs and spaces."
content_hash: b8953f0e012b8fdb8996d613bcc5500d8892cce0
last_modified_at: 2023-03-11
---
# stegsnow

Steganography tool for concealing and extracting messages in text files encoded as tabs and spaces.
More information: <https://darkside.com.au/snow/manual.html>.

- Extract [m]essage from file:

`stegsnow `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.txt</span>

- Extract [C]ompressed and [p]assword protected [m]essage from file:

`stegsnow -C -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">password</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.txt</span>

- Determine approximate [S]torage capacity with line [l]ength less than 72 for file:

`stegsnow -S -l 72 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.txt</span>

- Conceal [m]essage in text from file and save to result:

`stegsnow -m '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">message</span>`' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.txt</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/result.txt</span>

- Conceal message [f]ile content [C]ompressed in text from file and save to result:

`stegsnow -C -f '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/message.txt</span>`' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.txt</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/result.txt</span>

- Conceal [m]essage [C]ompressed and [p]assword protected in text from file and save to result:

`stegsnow -C -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">password</span>` -m '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">message</span>`' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.txt</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/result.txt</span>
