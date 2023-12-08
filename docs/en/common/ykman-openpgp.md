---
layout: page
title: common/ykman-openpgp (English)
description: "Manage the OpenPGP YubiKey application."
content_hash: 06a636d41d1129ea09c90200d621f1dec5acd28f
last_modified_at: 2023-12-08
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/ykman-openpgp.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># ykman openpgp

Manage the OpenPGP YubiKey application.
Note: you need to use `gpg --card-edit` for some settings.
More information: <https://docs.yubico.com/software/yubikey/tools/ykman/OpenPGP_Commands.html>.

- Display general information about the OpenPGP application:

`ykman openpgp info`

- Set the number of retry attempts for the User PIN, Reset Code, and Admin PIN, respectively:

`ykman openpgp access set-retries `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3</span>

- Change the User PIN, Reset Code or Admin PIN:

`ykman openpgp access change-`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pin|reset-code|admin-pin</span>

- Factory reset the OpenPGP application (you have to do this after exceeding the number of Admin PIN retry attempts):

`ykman openpgp reset`
