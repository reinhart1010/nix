---
layout: page
title: common/pssh (português (Brasil))
description: "Programa de SSH paralelo."
content_hash: e478f81c1555a9a29847c246e4fea8c854dadfd0
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/pssh.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pssh

Programa de SSH paralelo.
Mais informações: <https://manned.org/pssh>.

- Executar um comando em dois hosts e imprimir a saída em cada servidor em linha:

`pssh -i -H "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host2</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hostname -i</span>

- Executar um comando e salvar a saída em arquivos separados:

`pssh -H `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host1</span>` -H `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host2</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/diretório_de_saída</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hostname -i</span>

- Executar um comando em vários hosts, especificados em um arquivo separado por nova linha:

`pssh -i -h `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo_de_hosts</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hostname -i</span>

- Executar um comando como root (isso solicitará a senha do root):

`pssh -i -h `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo_de_hosts</span>` -A -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_de_usuário_do_root</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hostname -i</span>

- Executar um comando com argumentos SSH adicionais:

`pssh -i -h `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo_de_hosts</span>` -x "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-O VisualHostKey=yes</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hostname -i</span>

- Executar um comando limitando o número de conexões paralelas para 10:

`pssh -i -h `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo_de_hosts</span>` -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>` '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cd dir; ./script.sh; exit</span>`'`
