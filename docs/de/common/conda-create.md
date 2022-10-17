---
layout: page
title: common/conda-create (Deutsch)
description: "Erstelle neue Conda-Umgebungen."
content_hash: be3e8183476ae5d61b9d673ef1d748e6df248773
related_topics:
  - title: English version
    url: /en/common/conda-create.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># conda create

Erstelle neue Conda-Umgebungen.
Weitere Informationen: <https://docs.conda.io/projects/conda/en/latest/commands/create.html>.

- Erstelle eine neue Umgebung mit dem Namen `py39` und installiere Python 3.9 und NumPy v1.11 (oder höher) darin:

`conda create --yes --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">py39</span>` python=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3.9</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">numpy>=1.11</span>`"`

- Erstelle eine exakte Kopie einer Umgebung:

`conda create --clone `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">py39</span>` --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">py39-copy</span>

- Erstelle eine neue Umgebung mit gegebenem Namen und den zu installierenden Paketen:

`conda create --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">umgebungsname</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paketname</span>
