---
layout: page
title: linux/cryptsetup-open (English)
description: "Create a decrypted mapping of an encrypted volume."
content_hash: 79aace9077217a7a1fba4020ba0494933f446496
last_modified_at: 2024-10-17
tldri18n_status: 2
---
# cryptsetup open

Create a decrypted mapping of an encrypted volume.
Note: with TRIM enabled, minimal data leakage in form of freed block information, perhaps sufficient to determine the filesystem in use may occur.
However, you still most likely want to enable it, because the data inside is still safe and SSDs without TRIM will wear out faster.
More information: <https://manned.org/cryptsetup-open>.

- Open a LUKS volume and create a decrypted mapping at `/dev/mapper/mapping_name`:

`cryptsetup open `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdXY</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mapping_name</span>

- Use a keyfile instead of a passphrase:

`cryptsetup open --key-file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdXY</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mapping_name</span>

- Allow the use of TRIM on the device:

`cryptsetup open --allow-discards `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdXY</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mapping_name</span>

- Write the `--allow-discards` option into the LUKS header (the option will then always be used when you open the device):

`cryptsetup open --allow-discards --persistent `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdXY</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mapping_name</span>

- Open a LUKS volume and make the decrypted mapping read-only:

`cryptsetup open --readonly `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdXY</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mapping_name</span>
