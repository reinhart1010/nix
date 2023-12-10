---
layout: page
title: common/ykman-openpgp (Nederlands)
description: "Beheer de OpenPGP YubiKey applicatie."
content_hash: 0d166fef6ce2773f3f58422bae5483c75118e2c3
last_modified_at: 2023-12-10
related_topics:
  - title: English version
    url: /en/common/ykman-openpgp.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/ykman-openpgp.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># ykman openpgp

Beheer de OpenPGP YubiKey applicatie.
Opmerking: je dient `gpg --card-edit` te gebruiken voor sommige instellingen.
Meer informatie: <https://docs.yubico.com/software/yubikey/tools/ykman/OpenPGP_Commands.html>.

- Toon algemene informatie over de OpenPGP applicatie:

`ykman openpgp info`

- Stel het aantal herstelpogingen in voor de gebruikers pin, herstelcode en admin pin:

`ykman openpgp access set-retries `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3</span>

- Verander de gebruikers pin, herstelcode of admin pin:

`ykman openpgp access change-`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pin|reset-code|admin-pin</span>

- Herstel de OpenPGP applicatie naar fabrieksinstellingen (je moet dit doen nadat je het aantal pogingen voor de Admin pin hebt overschreden):

`ykman openpgp reset`
