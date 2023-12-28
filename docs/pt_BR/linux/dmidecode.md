---
layout: page
title: linux/dmidecode (português (Brasil))
description: "Exibe em formato de fácil leitura o sumário DMI (também conhecido como SMBIOS) ."
content_hash: b4208689d35b52125bb9f8b066889626bf2858ac
last_modified_at: 2023-12-28
related_topics:
  - title: català version
    url: /ca/linux/dmidecode.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/dmidecode.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/dmidecode.html
    icon: bi bi-globe
tldri18n_status: 2
---
# dmidecode

Exibe em formato de fácil leitura o sumário DMI (também conhecido como SMBIOS) .
Requer privilégio de super usuário.
Mais informações: <https://manned.org/dmidecode>.

- Exibe o sumário do DMI:

`sudo dmidecode`

- Exibe a versão da BIOS:

`sudo dmidecode -s bios-version`

- Exibe o número de série do sistema:

`sudo dmidecode -s system-serial-number`

- Exibe as informações da BIOS:

`sudo dmidecode -t bios`

- Exibe as informações da CPU:

`sudo dmidecode -t processor`

- Exibe as informações da memória:

`sudo dmidecode -t memory`
