---
layout: page
title: common/duc (português (Brasil))
description: "Uma coleção de ferramentas para indexar, inspecionar e visualizar uso do disco."
content_hash: 3d52078b965f2073990f137e1773152ec12177c5
last_modified_at: 2024-08-13
related_topics:
  - title: English version
    url: /en/common/duc.html
    icon: bi bi-globe
tldri18n_status: 2
---
# duc

Uma coleção de ferramentas para indexar, inspecionar e visualizar uso do disco.
O duc mantém uma base de dados dos tamanhos acumlados dos diretórios do sistema de arquivos, permitindo buscas nessa base, ou a criação de gráficos elegantes.
Mais informações: <https://duc.zevv.nl/>.

- Indexa o diretório /usr, escrevendo a base de dados para o local default em ~/.duc.db:

`duc index `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/usr</span>

- Lista todos os arquivos e diretórios dentro do /usr/local, mostrando tamanho relativo dos arquivos em um [g]raph (gráfico):

`duc ls -Fg `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/usr/local</span>

- Lista todos os arquivos e diretórios dentro do /usr/local em uma visão de árvore recursiva:

`duc ls -Fg -R `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/usr/local</span>

- Inicia uma interface gráfica para o usuário explorar o sistema de arquivos exibindo o gráfico sunburst:

`duc gui `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/usr</span>

- Executa a interface de console ncurses para explorar o sistema de arquivos:

`duc ui `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/usr</span>

- Exporta as informações da base de dados:

`duc info`
