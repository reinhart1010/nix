---
layout: page
title: linux/systemd-cryptenroll (English)
description: "Interactively enroll or remove methods used to unlock LUKS2-encrypted partitions/block devices."
content_hash: ad51c015693f0a600cef63d93e4873ff2f6d0f7e
last_modified_at: 2023-10-02
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># systemd-cryptenroll

Interactively enroll or remove methods used to unlock LUKS2-encrypted partitions/block devices.
In order to allow a partition to be unlocked during system boot using something other than a Password, also update the crypttab file and initramfs.
More information: <https://www.freedesktop.org/software/systemd/man/systemd-cryptenroll.html>.

- Unlock using Password, and enroll a new/additional Password:

`systemd-cryptenroll --password `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/luks2_block_device</span>

- Unlock using Password, and enroll a new/additional Recovery Key:

`systemd-cryptenroll --recovery-key `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/luks2_block_device</span>

- Unlock using Password, and list available or enroll a new/additional PKCS#11 Token:

`systemd-cryptenroll --pkcs11-token-uri=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">list|auto|pkcs11_token_uri</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/luks2_block_device</span>

- Unlock using Password, and list available or enroll a new FIDO2-Device (using PIN and Presence/Touch if available):

`systemd-cryptenroll --fido2-device=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">list|auto|path/to/fido2_hidraw_device</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/luks2_block_device</span>

- Unlock using Password, and enroll a new FIDO2-Device with User Verification (Biometrics):

`systemd-cryptenroll --fido2-device=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">auto|path/to/fido2_hidraw_device</span>` --fido2-with-user-verification=yes `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/luks2_block_device</span>

- Unlock using a FIDO2-Device, and enroll a new FIDO2-Device:

`systemd-cryptenroll --unlock-fido2-device=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/fido2_hidraw_unlock_device</span>` --fido2-device=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/fido2_hidraw_enroll_device</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/luks2_block_device</span>

- Unlock using Password, and enroll a TPM2 Security Chip (only secure-boot-policy PCR) and require additional alphanumeric PIN:

`systemd-cryptenroll --tpm2-device=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">auto|path/to/tpm2_block_device</span>` --tpm2-with-pin=yes `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/luks2_block_device</span>

- Unlock using Password, and remove all empty Passwords/all Passwords/all FIDO2-Devices/all PKCS#11 Tokens/all TMP2 Security Chips/all Recovery-Keys/all Methods:

`systemd-cryptenroll --wipe-slots=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">empty|password|fido2|pkcs#11|tpm2|recovery|all</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/luks2_block_device</span>
