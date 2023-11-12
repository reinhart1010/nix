---
layout: page
title: common/pyenv-virtualenv (italiano)
description: "Crea ambienti virtuali basati sulle distribuzioni Python che si hanno installate."
content_hash: 305297b7de14f5d793d5b36861de79df1f0596a0
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/pyenv-virtualenv.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pyenv virtualenv

Crea ambienti virtuali basati sulle distribuzioni Python che si hanno installate.
Maggiori informazioni: <https://github.com/pyenv/pyenv-virtualenv>.

- Crea un nuovo ambiente virtuale basato su Python 3.6.6:

`pyenv virtualenv `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3.6.6</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">virtualenv_name</span>

- Elenca tutti gli ambienti virtuali esistenti:

`pyenv virtualenvs`

- Attiva un ambiente virtuale:

`pyenv activate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">virtualenv_name</span>

- Disattiva l'ambiente virtuale corrente:

`pyenv deactivate`
