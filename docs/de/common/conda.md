---
layout: page
title: common/conda (Deutsch)
description: "Eine Paket-, Abhängigkeits- und Umgebungsverwaltung für beliebige Programmiersprachen."
content_hash: 6fd5c20d2eced14791bd8f50207817c6c4f83944
related_topics:
  - title: English version
    url: /en/common/conda.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/conda.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/conda.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># conda

Eine Paket-, Abhängigkeits- und Umgebungsverwaltung für beliebige Programmiersprachen.
Manche Unterbefehle wie `conda create` sind separat dokumentiert.
Weitere Informationen: <https://github.com/conda/conda>.

- Erstelle eine neue Umgebung mit den zu installierenden Paketen:

`conda create --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">umgebungsname</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">python=3.9 matplotlib</span>

- Liste alle Umgebungen auf:

`conda info --envs`

- Lade eine Umgebung:

`conda `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">activate umgebungs_name</span>

- Entlade eine Umgebung:

`conda `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">deactivate</span>

- Lösche eine Umgebung (entferne alle Pakete):

`conda remove --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">umgebungsname</span>` --all`

- Installiere Pakete in die derzeit geladene Umgebung:

`conda install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">python=3.4 numpy</span>

- Liste alle installierten Pakete in der derzeit geladenen Umgebung auf:

`conda list`

- Lösche alle ungenutzten Pakete und leere den Cache:

`conda clean --all`