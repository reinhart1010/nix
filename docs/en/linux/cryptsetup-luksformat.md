---
layout: page
title: linux/cryptsetup-luksformat (English)
description: "Initialize a LUKS partition and the initial key slot (0) with a passphrase or keyfile."
content_hash: bfb2a0fb9fae2b2d4682723278c9037c1f59bc66
last_modified_at: 2024-11-08
tldri18n_status: 2
---
# cryptsetup luksFormat

Initialize a LUKS partition and the initial key slot (0) with a passphrase or keyfile.
Note: this operation overwrites all data on the partition.
More information: <https://manned.org/cryptsetup-luksFormat>.

- Initialize a LUKS volume with a passphrase:

`cryptsetup luksFormat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdXY</span>

- Initialize a LUKS volume with a keyfile:

`cryptsetup luksFormat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdXY</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/keyfile</span>

- Initialize a LUKS volume with a passphrase and set its label:

`cryptsetup luksFormat --label `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">label</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdXY</span>
