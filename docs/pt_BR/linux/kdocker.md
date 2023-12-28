---
layout: page
title: linux/kdocker (português (Brasil))
description: "Ancorar facilmente aplicativos à bandeja do sistema."
content_hash: 95b747896c70e20de011a86f26b014c7afb39bd3
last_modified_at: 2023-12-28
related_topics:
  - title: English version
    url: /en/linux/kdocker.html
    icon: bi bi-globe
tldri18n_status: 2
---
# kdocker

Ancorar facilmente aplicativos à bandeja do sistema.
Mais informações: <https://github.com/user-none/KDocker>.

- Exibe um cursor que envia uma janela para a bandeja do sistema ao pressionar o botão esquerdo do mouse (pressione qualquer outro botão do mouse para cancelar):

`kdocker`

- Abre um aplicativo e o envia para a bandeja do sistema:

`kdocker `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">aplicativo</span>

- Envia a janela com foco para a bandeja do sistema:

`kdocker -f`

- Exibe um cursor que envia uma janela para a bandeja do sistema com um ícone personalizado ao pressionar o botão esquerdo do mouse:

`kdocker -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/caminho/para/ícone</span>

- Abre um aplicativo, envia-o para a bandeja do sistema e, se perder o foco, minimiza-o:

`kdocker -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">aplicativo</span>

- Exibe a versão:

`kdocker --version`
