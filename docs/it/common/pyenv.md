---
layout: page
title: common/pyenv (italiano)
description: "Passa da una distribuzione all'altra di Python in modo semplice."
content_hash: 8b164c80ae6bee7a3a780aff3bb400a9806a325f
related_topics:
  - title: English version
    url: /en/common/pyenv.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/pyenv.html
    icon: bi bi-globe
---
# pyenv

Passa da una distribuzione all'altra di Python in modo semplice.
Maggiori informazioni: <https://github.com/pyenv/pyenv>.

- Elenca i comandi disponibili:

`pyenv commands`

- Elenca tutte le distribuzioni di Python presenti nella cartella `${PYENV_ROOT}/versions`:

`pyenv versions`

- Elenca tutte le versioni di Python che possono essere installate da upstream:

`pyenv install --list`

- Installa una distribuzione di Python nella cartella `${PYENV_ROOT}/versions`:

`pyenv install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2.7.10</span>

- Disinstalla una distribuzione di Python dalla cartella `${PYENV_ROOT}/versions`:

`pyenv uninstall `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2.7.10</span>

- Imposta la distribuzione di Python da utilizzare globalmente sulla macchina:

`pyenv global `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2.7.10</span>

- Imposta la distribuzione di Python da utilizzare nella cartella corrente e in tutte le relative sottocartelle:

`pyenv local `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2.7.10</span>
