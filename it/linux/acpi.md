---
layout: page
title: linux/acpi (italiano)
description: "Mostra lo stato e le informazioni termiche della batteria."
content_hash: 4906e2a6aee5a668078e3ff351bcbdde5200f22a
related_topics:
  - title: Deutsch version
    url: /de/linux/acpi.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/acpi.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/acpi.html
    icon: bi bi-globe
---
# acpi

Mostra lo stato e le informazioni termiche della batteria.
Maggiori informazioni: <https://sourceforge.net/projects/acpiclient/files/acpiclient/>.

- Mostra le informazioni sulla batteria:

`acpi`

- Mostra le informazioni termiche:

`acpi -t`

- Mostra le informazioni sul dispositivo di raffreddamento:

`acpi -c`

- Mostra le informazioni termiche in gradi Fahrenheit:

`acpi -tf`

- Mostra tutte le informazioni:

`acpi -V`

- Estrae le informazioni da `/proc` invece che da `/sys`:

`acpi -p`
