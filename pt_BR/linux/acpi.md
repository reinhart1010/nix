---
layout: page
title: linux/acpi (português (Brasil))
description: "Exibe status da bateria ou informações térmicas."
content_hash: 2218d74621e1bee353512ef25907853486011351
related_topics:
  - title: català version
    url: /ca/linux/acpi.html
    icon: bi bi-globe
  - title: Deutsch version
    url: /de/linux/acpi.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/acpi.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/acpi.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/linux/acpi.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/acpi.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># acpi

Exibe status da bateria ou informações térmicas.
Mais informação: <https://sourceforge.net/projects/acpiclient/files/acpiclient/>.

- Exibe informações sobre a bateria:

`acpi`

- Exibe informações térmicas:

`acpi -t`

- Exibe informações sobre dispositivo de resfriamento:

`acpi -c`

- Exibe informações térmicas em Fahrenheit:

`acpi -tf`

- Exibe todas as informações:

`acpi -V`

- Extrai informações de `/proc` em vez de `/sys`:

`acpi -p`
