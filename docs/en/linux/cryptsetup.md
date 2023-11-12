---
layout: page
title: linux/cryptsetup (English)
description: "Manage plain dm-crypt and LUKS (Linux Unified Key Setup) encrypted volumes."
content_hash: 533f83f4fa2e2e3636b6cc525921840cbad6bc62
last_modified_at: 2023-11-12
related_topics:
  - title: 中文 version
    url: /zh/linux/cryptsetup.html
    icon: bi bi-globe
tldri18n_status: 2
---
# cryptsetup

Manage plain dm-crypt and LUKS (Linux Unified Key Setup) encrypted volumes.
More information: <https://gitlab.com/cryptsetup/cryptsetup/>.

- Initialize a LUKS volume (overwrites all data on the partition):

`cryptsetup luksFormat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sda1</span>

- Open a LUKS volume and create a decrypted mapping at `/dev/mapper/target`:

`cryptsetup luksOpen `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sda1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">target</span>

- Remove an existing mapping:

`cryptsetup luksClose `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">target</span>

- Change the LUKS volume's passphrase:

`cryptsetup luksChangeKey `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sda1</span>
