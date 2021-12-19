---
layout: page
title: linux/acpi (Deutsch)
description: "Zeigt den Akkustatus oder Temperatur-Informationen an."
content_hash: 486c566b3fb584e602487e68ff93ab887e1f6bf6
related_topics:
  - title: English version
    url: /en/linux/acpi.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/linux/acpi.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/acpi.html
    icon: bi bi-globe
---
# acpi

Zeigt den Akkustatus oder Temperatur-Informationen an.
Mehr Informationen: <https://sourceforge.net/projects/acpiclient/files/acpiclient/>.

- Zeige Informationen über den Akku an:

`acpi`

- Zeige Informationen zur Temperatur an:

`acpi -t`

- Zeige Informationen über die Kühlung an:

`acpi -c`

- Zeige Temperatur-Informationen in Fahrenheit an:

`acpi -tf`

- Zeige alle Informationen an:

`acpi -V`

- Extrahiere Informationen von `/proc`, anstatt von `/sys`:

`acpi -p`
