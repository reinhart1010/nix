---
layout: page
title: common/cabal (português (Brasil))
description: "Interface de linha de comando para a infraestrutura de pacote Haskel (Cabal)."
content_hash: 86f258161d383216349d6265bcabbc149f6a571b
last_modified_at: 2024-05-23
related_topics:
  - title: English version
    url: /en/common/cabal.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/cabal.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/cabal.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/cabal.html
    icon: bi bi-globe
tldri18n_status: 2
---
# cabal

Interface de linha de comando para a infraestrutura de pacote Haskel (Cabal).
Gerencia projetos Haskell e pacotes Cabal do repositório de pacotes Hackage.
Mais informações: <https://cabal.readthedocs.io/en/latest/getting-started.html>.

- Busca e lista pacotes do Hackage:

`cabal list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">string_buscada</span>

- Mostra informações sobre o pacote:

`cabal info `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_pacote</span>

- Baixa e instala um pacote:

`cabal install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_pacote</span>

- Cria um novo projeto Haskell no diretório atual:

`cabal init`

- Monta o projeto no diretório atual:

`cabal build`

- Roda testes do projeto no diretório atual:

`cabal test`
