---
layout: page
title: common/ykman-oath (Nederlands)
description: "Beheer de OATH YubiKey applicatie."
content_hash: 38a7b93b00b7e23e19976376e79d277f0f2b3149
last_modified_at: 2023-12-10
related_topics:
  - title: English version
    url: /en/common/ykman-oath.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/ykman-oath.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># ykman oath

Beheer de OATH YubiKey applicatie.
Een `keyword` kan onderdeel zijn van de naam of van de indiener.
Meer informatie: <https://docs.yubico.com/software/yubikey/tools/ykman/OATH_Commands.html>.

- Toon algemene informatie over de OATH applicatie:

`ykman oath info`

- Verander het wachtwoord dat de OATH accounts beschermd (voeg `--clear` toe om het te verwijderen):

`ykman oath access change`

- Voeg een nieuw account toe (`--issuer` is optioneel):

`ykman oath accounts add --issuer `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">indiener</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">naam</span>

- Toon alle accounts (met hun indiener):

`ykman oath accounts list`

- Toon alle accounts met hun huidige TOTP/HOTP codes (optioneel kan deze lijst gefilterd worden met een keyword):

`ykman oath accounts code `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">keyword</span>

- Hernoem een account:

`ykman oath accounts rename `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">keyword</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">indiener:naam|naam</span>

- Verwijder een account:

`ykman oath accounts delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">keyword</span>

- Verwijder alle accounts en herstel de fabrieksinstellingen:

`ykman oath reset`
