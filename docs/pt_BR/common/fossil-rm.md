---
layout: page
title: common/fossil-rm (português (Brasil))
description: "Remove arquivos ou diretórios do controle de versão do Fossil."
content_hash: 6cff7a7c48e77e100a8d1264568e94ecc9407c0c
last_modified_at: 2024-10-12
related_topics:
  - title: English version
    url: /en/common/fossil-rm.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/fossil-rm.html
    icon: bi bi-globe
tldri18n_status: 2
---
# fossil rm

Remove arquivos ou diretórios do controle de versão do Fossil.
Veja também: `fossil forget`.
Mais informações: <https://fossil-scm.org/home/help/rm>.

- Remove um arquivo ou diretório do controle de versão do Fossil:

`fossil rm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo_ou_diretório</span>

- Remove um arquivo ou diretório do controle de versão do Fossil e também o exclui do disco:

`fossil rm --hard `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo_ou_diretório</span>

- Adiciona novamente todos os arquivos removidos e dos quais não se fez commit anteriormente ao controle de versão do Fossil:

`fossil rm --reset`
