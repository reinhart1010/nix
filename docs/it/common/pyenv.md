---
layout: page
title: common/pyenv (italiano)
description: "Passa da una distribuzione all'altra di Python in modo semplice."
content_hash: f61518b6929c34aeef252593660ff9e08de365d7
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/pyenv.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/pyenv.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/pyenv.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pyenv

Passa da una distribuzione all'altra di Python in modo semplice.
Maggiori informazioni: <https://github.com/pyenv/pyenv>.

- Elenca i comandi disponibili:

`pyenv commands`

- Elenca tutte le distribuzioni di Python presenti nella directory `${PYENV_ROOT}/versions`:

`pyenv versions`

- Elenca tutte le versioni di Python che possono essere installate da upstream:

`pyenv install --list`

- Installa una distribuzione di Python nella directory `${PYENV_ROOT}/versions`:

`pyenv install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2.7.10</span>

- Disinstalla una distribuzione di Python dalla directory `${PYENV_ROOT}/versions`:

`pyenv uninstall `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2.7.10</span>

- Imposta la distribuzione di Python da utilizzare globalmente sulla macchina:

`pyenv global `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2.7.10</span>

- Imposta la distribuzione di Python da utilizzare nella directory corrente e in tutte le relative sottodirectory:

`pyenv local `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2.7.10</span>
