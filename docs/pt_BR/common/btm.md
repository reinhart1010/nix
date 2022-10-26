---
layout: page
title: common/btm (português (Brasil))
description: "Uma alternativa ao `top`."
content_hash: 825ac17b25b7f040428b56b939894e52798b2922
related_topics:
  - title: English version
    url: /en/common/btm.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/btm.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># btm

Uma alternativa ao `top`.
Tem como objetivo ser leve, multiplataforma e mais gráfico que o `top`.
Mais informações: <https://github.com/ClementTsang/bottom>.

- Exibe o layout padrão (CPU, memória, temperaturas, disco, rede e processos):

`btm`

- Ativa o modo básico, removendo gráficos e condensando dados (semelhante a `top`):

`btm --basic`

- Usa pontos grandes em vez de pequenos em gráficos:

`btm --dot_marker`

- Exibe também a carga da bateria e o estado de saúde:

`btm --battery`

- Atualiza a cada 250 milissegundos e exibe os últimos 30 segundos nos gráficos:

`btm --rate 250 --default_time_value 30000`
