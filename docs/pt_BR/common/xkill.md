---
layout: page
title: common/xkill (português (Brasil))
description: "Termina uma janela interativamente em uma sessão gráfica."
content_hash: 2ef49e3eaf3f3b2fbd754664e887d685e881dce7
last_modified_at: 2024-01-03
related_topics:
  - title: English version
    url: /en/common/xkill.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/xkill.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/xkill.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/xkill.html
    icon: bi bi-globe
  - title: português (Portugal) version
    url: /pt_PT/common/xkill.html
    icon: bi bi-globe
tldri18n_status: 2
---
# xkill

Termina uma janela interativamente em uma sessão gráfica.
Veja também: `kill`, `killall`.
Mais informações: <https://www.x.org/releases/current/doc/man/man1/xkill.1.xhtml>.

- Ativa um cursor para fechar uma janela com o clique do botão esquerdo do mouse (pressionar qualquer outro botão para cancelar):

`xkill`

- Mostra um cursor para selecionar uma janela pressionando qualquer botão do mouse:

`xkill -button any`

- Fecha uma janela com um id específico (use `xwininfo` para obter informações sobre janelas):

`xkill -id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id</span>
