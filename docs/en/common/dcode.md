---
layout: page
title: common/dcode (English)
description: "Recursively detect and decode strings, supporting hex, decimal, binary, base64, URL, FromChar encodings, Caesar ciphers, and MD5, SHA1, and SHA2 hashes."
content_hash: 2a8d6fd763afec2cb8e03fff2a421bba1c7788f4
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# dcode

Recursively detect and decode strings, supporting hex, decimal, binary, base64, URL, FromChar encodings, Caesar ciphers, and MD5, SHA1, and SHA2 hashes.
Warning: uses 3rd-party web services for MD5, SHA1 and SHA2 hash lookups. For sensitive data, use `-s` to avoid these services.
More information: <https://github.com/s0md3v/Decodify>.

- Recursively detect and decode a string:

`dcode "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">NjM3YTQyNzQ1YTQ0NGUzMg==</span>`"`

- Rotate a string by the specified offset:

`dcode -rot `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">11</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">spwwz hzcwo</span>`"`

- Rotate a string by all 26 possible offsets:

`dcode -rot `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">all</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bpgkta xh qtiitg iwpc sr</span>`"`

- Reverse a string:

`dcode -rev "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hello world</span>`"`
