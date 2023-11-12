---
layout: page
title: common/gmssl (English)
description: "GmSSL is a crypto toolkit supporting SM1, SM2, SM3, SM4, SM9, and ZUC/ZUC256."
content_hash: c24f13b19ea53583ae58fa195e9633676e140242
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# gmssl

GmSSL is a crypto toolkit supporting SM1, SM2, SM3, SM4, SM9, and ZUC/ZUC256.
More information: <http://gmssl.org/english.html>.

- Generate an SM3 hash for a file:

`gmssl sm3 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Encrypt a file using the SM4 cipher:

`gmssl sms4 -e -in `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>` -out `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.sms4</span>

- Decrypt a file using the SM4 cipher:

`gmssl sms4 -d -in `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.sms4</span>

- Generate an SM2 private key:

`gmssl sm2 -genkey -out `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.pem</span>

- Generate an SM2 public key from an existing private key:

`gmssl sm2 -pubout -in `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.pem</span>` -out `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.pem.pub</span>

- Encrypt a file using the ZUC cipher:

`gmssl zuc -e -in `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>` -out `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.zuc</span>

- Decrypt a file using the ZUC cipher:

`gmssl zuc -d -in `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.zuc</span>

- Print version:

`gmssl version`
