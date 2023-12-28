---
layout: page
title: common/docker-update (português (Brasil))
description: "Atualizar a configuração de contêineres Docker."
content_hash: 8fe69a95a92bb871f00a07b136e114b712326492
last_modified_at: 2023-12-28
related_topics:
  - title: English version
    url: /en/common/docker-update.html
    icon: bi bi-globe
tldri18n_status: 2
---
# docker update

Atualizar a configuração de contêineres Docker.
Este comando não é suportado para contêineres Windows.
Mais informações: <https://docs.docker.com/engine/reference/commandline/update/>.

- Atualiza a política de reinicialização a ser aplicada quando um contêiner específico for encerrado:

`docker update --restart=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">always|no|on-failure|unless-stopped</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_contêiner</span>

- Atualiza a política para reiniciar até três vezes um contêiner específico quando ele for encerrado com status de saída diferente de zero:

`docker update --restart=on-failure:3 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_contêiner</span>

- Atualiza o número de CPUs disponíveis para um contêiner específico:

`docker update --cpus `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">quantidade</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_contêiner</span>

- Atualiza o limite de memória em [M]egabytes para um contêiner específico:

`docker update --memory `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">limite</span>`M `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_contêiner</span>

- Atualiza o número máximo de IDs de processos permitidos dentro de um contêiner específico (use `-1` para ilimitado):

`docker update --pids-limit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">quantidade</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_contêiner</span>

- Atualiza a quantidade de memória em [M]egabytes que um contêiner específico pode trocar para o disco (use `-1` para ilimitado):

`docker update --memory-swap `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">limite</span>`M `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_contêiner</span>
