---
layout: page
title: linux/sport (português (Brasil))
description: "Busque e instale Slackbuilds."
content_hash: dc0421f3a2ff4d5f7fb340684e7accf43bbbe5ec
last_modified_at: 2023-12-30
related_topics:
  - title: English version
    url: /en/linux/sport.html
    icon: bi bi-globe
tldri18n_status: 2
---
# sport

Busque e instale Slackbuilds.
Mais informações: <http://slackermedia.info/handbook/doku.php?id=slackbuilds>.

- Puxa a lista de SlackBuilds para rodar `sport` pela primeira vez:

`sudo mkdir -p /usr/ports && sudo rsync -av rsync://slackbuilds.org /slackbuilds/$(awk '{print $2}' /etc/slackware-version)/ /usr/ports/`

- Puxa qualquer atualização para a árvore do sistema via `rsync`:

`sudo sport rsync`

- Procura um pacote pelo nome:

`sport search "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">palavra_chave</span>`"`

- Checa se um pacote está instalado:

`sport check `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pacote</span>

- Exibe os arquivos README e `.info` de um pacote:

`sport cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pacote</span>

- Instala um pacote uma vez que as dependências estejam instaladas:

`sudo sport install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pacote</span>

- Instala uma lista de pacotes de um arquivo (formato: pacotes separados por espaço):

`sudo sport install $(< `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/lista</span>`)`
