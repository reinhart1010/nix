---
layout: page
title: common/pip-uninstall (português (Brasil))
description: "Desinstala pacotes Python."
content_hash: 592a26a2e10a04e7e692b0008a206380ea37df3e
related_topics:
  - title: English version
    url: /en/common/pip-uninstall.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># pip uninstall

Desinstala pacotes Python.
Mais informações: <https://pip.pypa.io>.

- Desinstala um pacote:

`pip uninstall `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_pacote</span>

- Desinstala pacotes listados em um arquivo:

`pip uninstall --requirement `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">requirements.txt</span>

- Desinstala um pacote sem pedir por confirmação:

`pip uninstall --yes `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_pacote</span>
