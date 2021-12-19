---
layout: page
title: windows/choco-pin (Deutsch)
description: "Hefte ein Chocolatey-Paket bei einer bestimmten Version an."
content_hash: dace2ed4434151d62925a5aa110fc5801fea1faf
related_topics:
  - title: English version
    url: /en/windows/choco-pin.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/choco-pin.html
    icon: bi bi-globe
---
# choco pin

Hefte ein Chocolatey-Paket bei einer bestimmten Version an.
Angeheftete Pakete werden nicht weiter aktualisiert.
Weitere Informationen: <https://chocolatey.org/docs/commands-pin>.

- Zeige eine Liste der angehefteten Pakete und ihrer Versionen an:

`choco pin list`

- Hefte ein Paket in der installierten Version an:

`choco pin add --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paket</span>

- Hefte ein Paket in einer bestimmten Version an:

`choco pin add --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paket</span>` --version `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">version</span>

- Entferne die Anheftung für ein bestimmtes Paket:

`choco pin remove --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paket</span>
