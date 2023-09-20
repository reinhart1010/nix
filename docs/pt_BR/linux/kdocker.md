---
layout: page
title: linux/kdocker (português (Brasil))
description: "Ancorar facilmente aplicativos à bandeja do sistema."
content_hash: a4aa5eaf2d17c3de1225906e294f5066038a2a15
last_modified_at: 2023-09-20
related_topics:
  - title: English version
    url: /en/linux/kdocker.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># kdocker

Ancorar facilmente aplicativos à bandeja do sistema.
Mais informações: <https://github.com/user-none/KDocker>.

- Exibir um cursor para enviar uma janela para a bandeja do sistema ao pressionar o botão esquerdo do mouse (pressione qualquer outro botão do mouse para cancelar):

`kdocker`

- Abrir um aplicativo e enviá-lo para a bandeja do sistema:

`kdocker `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">aplicativo</span>

- Enviar a janela com foco para a bandeja do sistema:

`kdocker -f`

- Exibir um cursor para enviar uma janela para a bandeja do sistema com um ícone personalizado ao pressionar o botão esquerdo do mouse:

`kdocker -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/caminho/para/ícone</span>

- Abrir um aplicativo, enviá-lo para a bandeja do sistema e, se perder o foco, minimizá-lo:

`kdocker -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">aplicativo</span>

- Exibir a versão:

`kdocker --version`
