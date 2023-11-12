---
layout: page
title: linux/dmidecode (català)
description: "Mostra la taula de continguts del DMI (també conegut com SMBIOS) en un format llegible per humans."
content_hash: a933397c242110f5c3cfd5390929acea2ed85267
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/linux/dmidecode.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/dmidecode.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/dmidecode.html
    icon: bi bi-globe
tldri18n_status: 2
---
# dmidecode

Mostra la taula de continguts del DMI (també conegut com SMBIOS) en un format llegible per humans.
Requereix privilegis de root.
Més informació: <https://manned.org/dmidecode>.

- Mostra tota la taula de continguts del DMI:

`sudo dmidecode`

- Mostra la versió de la BIOS:

`sudo dmidecode -s bios-version`

- Mostra el número de sèrie del equip:

`sudo dmidecode -s system-serial-number`

- Mostra informació de la BIOS:

`sudo dmidecode -t bios`

- Mostra informació de la CPU:

`sudo dmidecode -t processor`

- Mostra informació de la memòria:

`sudo dmidecode -t memory`
