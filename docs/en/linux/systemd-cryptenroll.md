---
layout: page
title: linux/systemd-cryptenroll (English)
description: "Interactively enroll or remove methods used to unlock LUKS2-encrypted devices. Uses a password to unlock the device unless otherwise specified."
content_hash: bc3b2b506584b2e88985d0d3083fd1a28ed13c32
last_modified_at: 2023-11-26
tldri18n_status: 2
---
# systemd-cryptenroll

Interactively enroll or remove methods used to unlock LUKS2-encrypted devices. Uses a password to unlock the device unless otherwise specified.
In order to allow a partition to be unlocked during system boot, update the `/etc/crypttab` file or the initramfs.
More information: <https://www.freedesktop.org/software/systemd/man/systemd-cryptenroll.html>.

- Enroll a new password (similar to `cryptsetup luksAddKey`):

`systemd-cryptenroll --password `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/luks2_block_device</span>

- Enroll a new recovery key (i.e. a randomly generated passphrase that can be used as a fallback):

`systemd-cryptenroll --recovery-key `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/luks2_block_device</span>

- List available tokens, or enroll a new PKCS#11 token:

`systemd-cryptenroll --pkcs11-token-uri `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">list|auto|pkcs11_token_uri</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/luks2_block_device</span>

- List available FIDO2 devices, or enroll a new FIDO2 device (`auto` can be used as the device name when there is only one token plugged in):

`systemd-cryptenroll --fido2-device `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">list|auto|path/to/fido2_hidraw_device</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/luks2_block_device</span>

- Enroll a new FIDO2 device with user verification (biometrics):

`systemd-cryptenroll --fido2-device `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">auto|path/to/fido2_hidraw_device</span>` --fido2-with-user-verification yes `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/luks2_block_device</span>

- Unlock using a FIDO2 device, and enroll a new FIDO2 device:

`systemd-cryptenroll --unlock-fido2-device `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/fido2_hidraw_unlock_device</span>` --fido2-device `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/fido2_hidraw_enroll_device</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/luks2_block_device</span>

- Enroll a TPM2 security chip (only secure-boot-policy PCR) and require an additional alphanumeric PIN:

`systemd-cryptenroll --tpm2-device `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">auto|path/to/tpm2_block_device</span>` --tpm2-with-pin yes `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/luks2_block_device</span>

- Remove all empty passwords/all passwords/all FIDO2 devices/all PKCS#11 tokens/all TPM2 security chips/all recovery keys/all methods:

`systemd-cryptenroll --wipe-slot `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">empty|password|fido2|pkcs#11|tpm2|recovery|all</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/luks2_block_device</span>
