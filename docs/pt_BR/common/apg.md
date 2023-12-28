---
layout: page
title: common/apg (português (Brasil))
description: "Criar senhas aleatórias arbitrariamente complexas."
content_hash: dfd0fe250351f9dd7b7b7582d34c99d056bd10ca
last_modified_at: 2023-12-28
related_topics:
  - title: English version
    url: /en/common/apg.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/apg.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/apg.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/apg.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/apg.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/apg.html
    icon: bi bi-globe
tldri18n_status: 2
---
# apg

Criar senhas aleatórias arbitrariamente complexas.
Mais informações: <https://manned.org/apg>.

- Cria senha aleatória (tamanho padrão para as senhas é 8 caracteres):

`apg`

- Cria senha com pelo menos 1 símbolo (S), 1 número (N), 1 letra maiúscula (C), 1 letra minúscula (L):

`apg -M SNCL`

- Cria uma senha com 16 caracteres:

`apg -m `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">16</span>

- Cria senha com tamanho máximo de 16 caracteres:

`apg -x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">16</span>

- Cria uma senha que não aparece em um dicionário provido pelo usuário:

`apg -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo_de_dicionario</span>
