---
layout: page
title: linux/systemd-cryptsetup (English)
description: "Create or remove decrypted mappings of encrypted volumes. Equivalent of `cryptsetup open` and `cryptsetup close`."
content_hash: dd77d7003fcccd52aea7ef869d30affbfaa36462
last_modified_at: 2024-12-08
tldri18n_status: 2
---
# systemd-cryptsetup

Create or remove decrypted mappings of encrypted volumes. Equivalent of `cryptsetup open` and `cryptsetup close`.
Arguments to this command are written exactly like a line in `/etc/crypttab`. It's used by systemd to unlock devices on boot.
See also: `cryptsetup`.
More information: <https://www.freedesktop.org/software/systemd/man/latest/systemd-cryptsetup.html>.

- Open a LUKS volume and create a decrypted mapping at `/dev/mapper/mapping_name`:

`systemd-cryptsetup attach `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mapping_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdXY</span>

- Open a LUKS volume with additional options and create a decrypted mapping at `/dev/mapper/mapping_name`:

`systemd-cryptsetup attach `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mapping_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdXY</span>` none `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">crypttab_options</span>

- Open a LUKS volume with a keyfile and create a decrypted mapping at `/dev/mapper/mapping_name`:

`systemd-cryptsetup attach `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mapping_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdXY</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/keyfile</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">crypttab_options</span>

- Remove an existing mapping:

`systemd-cryptsetup detach `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mapping_name</span>
