---
layout: page
title: common/ykman (Nederlands)
description: "YubiKey Manager - configureer YubiKeys."
content_hash: 721a6663d053ad0210a015af514302ed91d5ef47
last_modified_at: 2024-10-10
related_topics:
  - title: English version
    url: /en/common/ykman.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ykman

YubiKey Manager - configureer YubiKeys.
Als er meerdere YubiKeys zijn verbonden, dien je `--device serial_number` toe te voegen voor een subcommando.
Meer informatie: <https://docs.yubico.com/software/yubikey/tools/ykman/index.html>.

- Toon algemene informatie over een YubiKey (serienummer, firmware versie, mogelijkheden etc.):

`ykman info`

- Toon alle verbonden YubiKeys met een korte, een-regel beschrijving (inclusief het serienummer):

`ykman list`

- Bekijk de documentatie voor het in- en uitschakelen van applicaties:

`tldr ykman config`

- Bekijk de documentatie voor het beheren van de FIDO applicaties:

`tldr ykman fido`

- Bekijk de documentatie voor het beheren van de OATH applicatie:

`tldr ykman oath`

- Bekijk de documentatie voor het beheren van de OpenPGP applicatie:

`tldr ykman openpgp`
