---
layout: page
title: linux/dmidecode (português (Brasil))
description: "Exibe em formato de fácil leitura o sumário DMI (também conhecido como SMBIOS) ."
content_hash: 57815451261eadbd872131c0a1f2011a079c1873
related_topics:
  - title: English version
    url: /en/linux/dmidecode.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/dmidecode.html
    icon: bi bi-globe
---
# dmidecode

Exibe em formato de fácil leitura o sumário DMI (também conhecido como SMBIOS) .
Requer privilégio de super usuário.
Mais informações: <https://manned.org/dmidecode>.

- Exibir o sumário do DMI:

`sudo dmidecode`

- Exibir a versão da BIOS:

`sudo dmidecode -s bios-version`

- Exibir o número de série do sistema:

`sudo dmidecode -s system-serial-number`

- Exibir as informações da BIOS:

`sudo dmidecode -t bios`

- Exibir as informações da CPU:

`sudo dmidecode -t processor`

- Exibir as informações da memória:

`sudo dmidecode -t memory`
