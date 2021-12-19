---
layout: page
title: windows/choco-uninstall (Deutsch)
description: "Deinstalliere mit Chocolatey ein oder mehrere Pakete."
content_hash: 6fc9dfdba77ebb10ed446126ab7d8757c56d6484
related_topics:
  - title: English version
    url: /en/windows/choco-uninstall.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/windows/choco-uninstall.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/choco-uninstall.html
    icon: bi bi-globe
---
# choco uninstall

Deinstalliere mit Chocolatey ein oder mehrere Pakete.
Weitere Informationen: <https://chocolatey.org/docs/commands-uninstall>.

- Deinstalliere ein oder mehrere Pakete, deren Namen mit Leerzeichen getrennt sind:

`choco uninstall `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paket(e)</span>

- Deinstalliere eine bestimmte Version eines Paketes:

`choco uninstall `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paket</span>` --version `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">version</span>

- Stimme allen Fragen automatisch zu:

`choco uninstall `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paket</span>` --yes`

- Deinstalliere auch alle Abhängigkeiten:

`choco uninstall `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paket</span>` --remove-dependencies`

- Deinstalliere alle Pakete:

`choco uninstall all`
