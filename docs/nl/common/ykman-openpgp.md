---
layout: page
title: common/ykman-openpgp (Nederlands)
description: "Beheer de OpenPGP YubiKey applicatie."
content_hash: 0d166fef6ce2773f3f58422bae5483c75118e2c3
last_modified_at: 2023-12-11
related_topics:
  - title: English version
    url: /en/common/ykman-openpgp.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ykman openpgp

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
