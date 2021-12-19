---
layout: page
title: linux/cryptsetup (English)
description: "Manage plain dm-crypt and LUKS (Linux Unified Key Setup) encrypted volumes."
content_hash: 6410e43a128a78b564b917854b1c5c673f106c5c
---
# cryptsetup

Manage plain dm-crypt and LUKS (Linux Unified Key Setup) encrypted volumes.
More information: <https://gitlab.com/cryptsetup/cryptsetup/>.

- Initialize a LUKS volume (overwrites all data on the partition):

`cryptsetup luksFormat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sda1</span>

- Open a LUKS volume and create a decrypted mapping at `/dev/mapper/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">target</span>:

`cryptsetup luksOpen `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sda1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">target</span>

- Remove an existing mapping:

`cryptsetup luksClose `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">target</span>

- Change the LUKS volume's passphrase:

`cryptsetup luksChangeKey `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sda1</span>
