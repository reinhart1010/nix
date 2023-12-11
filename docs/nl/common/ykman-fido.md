---
layout: page
title: common/ykman-fido (Nederlands)
description: "Beheer YubiKey FIDO applicaties."
content_hash: 14a2ab9788f2fc744897557c0fd1cd0e5a13b1f5
last_modified_at: 2023-12-11
related_topics:
  - title: English version
    url: /en/common/ykman-fido.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ykman fido

Beheer YubiKey FIDO applicaties.
Meer informatie: <https://docs.yubico.com/software/yubikey/tools/ykman/FIDO_Commands.html>.

- Toon algemene informatie over de FIDO2 applicatie:

`ykman fido info`

- Verander de FIDO pin:

`ykman fido access change-pin`

- Toon een lijst van inloggegevens die opgeslagen zijn op de YubiKey:

`ykman fido credentials list`

- Verwijder specifieke inloggegevens van de YubiKey:

`ykman fido credentials delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id</span>

- Toon vingerafdrukken opgeslagen op de YubiKey (vereist een sleutel met een vingerafdruk sensor):

`ykman fido fingerprints list`

- Voeg een nieuwe vingerafdruk toe aan de YubiKey:

`ykman fido fingerprints add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">naam</span>

- Verwijder een vingerafdruk van de YubiKey:

`ykman fido fingerprints delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">naam</span>

- Wis alle FIDO credentials (je moet dit doen nadat je het aantal pogingen voor de pin hebt overschreden):

`ykman fido reset`
