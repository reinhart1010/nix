---
layout: page
title: linux/cryptsetup (English)
description: "Manage plain `dm-crypt` and LUKS (Linux Unified Key Setup) encrypted volumes."
content_hash: 44aded2f59282f5d5bfbe6c077691d6bad25df41
last_modified_at: 2024-10-16
related_topics:
  - title: 中文 version
    url: /zh/linux/cryptsetup.html
    icon: bi bi-globe
tldri18n_status: 2
---
# cryptsetup

Manage plain `dm-crypt` and LUKS (Linux Unified Key Setup) encrypted volumes.
Some subcommands such as `luksFormat` have their own usage documentation.
More information: <https://manned.org/cryptsetup>.

- Initialize a LUKS volume with a passphrase (overwrites all data on the partition):

`cryptsetup luksFormat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdXY</span>

- Open a LUKS volume and create a decrypted mapping at `/dev/mapper/mapping_name`:

`cryptsetup open `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdXY</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mapping_name</span>

- Display information about a mapping:

`cryptsetup status `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mapping_name</span>

- Remove an existing mapping:

`cryptsetup close `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mapping_name</span>

- Change a LUKS volume's passphrase:

`cryptsetup luksChangeKey `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdXY</span>
