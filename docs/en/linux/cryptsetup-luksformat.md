---
layout: page
title: linux/cryptsetup-luksformat (English)
description: "Initialize a LUKS partition and the initial key slot (0) with a passphrase or keyfile."
content_hash: 9c2ab025142260c1c63486169bd110e32dbbebfd
last_modified_at: 2024-10-17
tldri18n_status: 2
---
# cryptsetup luksFormat

Initialize a LUKS partition and the initial key slot (0) with a passphrase or keyfile.
Note: this operation overwrites all data on the partition.
More information: <https://manned.org/cryptsetup-luksFormat>.

- Initialize a LUKS volume with a passphrase:

`cryptsetup luksFormat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdXY</span>

- Initialize a LUKS volume with a keyfile:

`crypsetup luksFormat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdXY</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/keyfile</span>

- Initialize a LUKS volume with a passphrase and set its label:

`cryptsetup luksFormat --label `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">label</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdXY</span>
