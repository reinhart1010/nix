---
layout: page
title: common/dvc-checkout (português (Brasil))
description: "Registra a saída de arquivos e diretórios de dados vindos do cache."
content_hash: 1698df2e229170f5028a37b933b45d679937a92a
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/dvc-checkout.html
    icon: bi bi-globe
tldri18n_status: 2
---
# dvc checkout

Registra a saída de arquivos e diretórios de dados vindos do cache.
Mais informações: <https://dvc.org/doc/command-reference/checkout>.

- Registra a saída de todos os arquivos e diretórios de dados:

`dvc checkout`

- Registra a saída da última versão de um alvo específico:

`dvc checkout `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">alvo</span>

- Registra a saída de versão específica de um alvo de um commit/tag/branch Git:

`git checkout `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hash_do_commit|tag|branch</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">alvo</span>` && dvc checkout `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">alvo</span>
