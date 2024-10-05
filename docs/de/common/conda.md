---
layout: page
title: common/conda (Deutsch)
description: "Eine Paket-, Abhängigkeits- und Umgebungsverwaltung für beliebige Programmiersprachen."
content_hash: 6616499581e568a250d8ce63569afa7b65eb0172
last_modified_at: 2024-10-05
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
tldri18n_status: 2
---
# conda

Eine Paket-, Abhängigkeits- und Umgebungsverwaltung für beliebige Programmiersprachen.
Manche Unterbefehle wie `create` sind separat dokumentiert.
Weitere Informationen: <https://github.com/conda/conda>.

- Erstelle eine neue Umgebung mit den zu installierenden Paketen:

`conda create --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">umgebungsname</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">python=3.9 matplotlib</span>

- Liste alle Umgebungen auf:

`conda info --envs`

- Lade eine Umgebung:

`conda activate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">umgebungs_name</span>

- Entlade eine Umgebung:

`conda deactivate`

- Lösche eine Umgebung (entferne alle Pakete):

`conda remove --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">umgebungsname</span>` --all`

- Installiere Pakete in die derzeit geladene Umgebung:

`conda install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">python=3.4 numpy</span>

- Liste alle installierten Pakete in der derzeit geladenen Umgebung auf:

`conda list`

- Lösche alle ungenutzten Pakete und leere den Cache:

`conda clean --all`
