---
layout: page
title: common/ykman-oath (English)
description: "Manage the OATH YubiKey application."
content_hash: 341721f6382a66675029b3a54afda4f54a93749b
last_modified_at: 2023-12-09
tldri18n_status: 2
---
# ykman oath

Manage the OATH YubiKey application.
A `keyword` can be a part of the name or the issuer.
More information: <https://docs.yubico.com/software/yubikey/tools/ykman/OATH_Commands.html>.

- Display general information about the OATH application:

`ykman oath info`

- Change the password used to protect OATH accounts (add `--clear` to remove it):

`ykman oath access change`

- Add a new account (`--issuer` is optional):

`ykman oath accounts add --issuer `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">issuer</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>

- List all accounts (with their issuers):

`ykman oath accounts list`

- List all accounts with their current TOTP/HOTP codes (optionally filtering the list with a keyword):

`ykman oath accounts code `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">keyword</span>

- Rename an account:

`ykman oath accounts rename `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">keyword</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">issuer:name|name</span>

- Delete an account:

`ykman oath accounts delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">keyword</span>

- Delete all accounts and restore factory settings:

`ykman oath reset`
