---
layout: page
title: linux/bootc (português (Brasil))
description: "Inicializa e atualiza seu sistema usando imagens de containeres."
content_hash: bb7b723d2373d8578da52317325cfc41f53d386d
last_modified_at: 2024-11-25
related_topics:
  - title: English version
    url: /en/linux/bootc.html
    icon: bi bi-globe
tldri18n_status: 2
---
# bootc

Inicializa e atualiza seu sistema usando imagens de containeres.
Manipula atualizações transacionais e transparentes utilizando imagens de containeres OCI/Docker.
Mais informações: <https://containers.github.io/bootc/>.

- Mostra todos os deployments na ordem que eles aparecem na inicialização:

`bootc status`

- Mostra se há alguma atualização disponível:

`bootc upgrade --check`

- Atualiza e reinicia o sistema:

`bootc upgrade --apply`

- Move seu sistema para outra base:

`bootc switch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">imagem</span>

- Reinicia o seu sistema no deployment anterior:

`bootc rollback`
