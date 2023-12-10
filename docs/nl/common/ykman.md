---
layout: page
title: common/ykman (Nederlands)
description: "YubiKey Manager - configureer YubiKeys."
content_hash: 829262d5312007ef225c54c880ddb197fd1e502f
last_modified_at: 2023-12-10
related_topics:
  - title: English version
    url: /en/common/ykman.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/ykman.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># ykman

YubiKey Manager - configureer YubiKeys.
Als er meerdere YubiKeys zijn verbonden, dien je `--device serial_number` toe te voegen voor een subcommando.
Meer informatie: <https://docs.yubico.com/software/yubikey/tools/ykman/index.html>.

- Toon algemene informatie over een  YubiKey (serienummer, firmware versie, mogelijkheden etc.):

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
