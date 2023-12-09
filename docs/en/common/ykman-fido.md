---
layout: page
title: common/ykman-fido (English)
description: "Manage YubiKey FIDO applications."
content_hash: 70384c182ab6c41b9dead47adbfa20318422cdee
last_modified_at: 2023-12-09
tldri18n_status: 2
---
# ykman fido

Manage YubiKey FIDO applications.
More information: <https://docs.yubico.com/software/yubikey/tools/ykman/FIDO_Commands.html>.

- Display general information about the FIDO2 application:

`ykman fido info`

- Change the FIDO pin:

`ykman fido access change-pin`

- List resident credentials stored on the YubiKey:

`ykman fido credentials list`

- Delete a resident credential from the YubiKey:

`ykman fido credentials delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id</span>

- List fingerprints stored on the YubiKey (requires a key with a fingerprint sensor):

`ykman fido fingerprints list`

- Add a new fingerprint to the YubiKey:

`ykman fido fingerprints add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>

- Delete a fingerprint from the YubiKey:

`ykman fido fingerprints delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>

- Wipe all FIDO credentials (you have to do this after exceeding the number of PIN retry attempts):

`ykman fido reset`
