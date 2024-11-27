---
layout: page
title: common/accelerate (português (Brasil))
description: "Uma biblioteca que habilita o mesmo código PyTorch a rodar em qualquer configuração distribuída."
content_hash: f570084a891bd44fcd156d70cb1308bcc6a6baee
last_modified_at: 2024-11-27
related_topics:
  - title: English version
    url: /en/common/accelerate.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/accelerate.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/accelerate.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/accelerate.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/accelerate.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/accelerate.html
    icon: bi bi-globe
tldri18n_status: 2
---
# accelerate

Uma biblioteca que habilita o mesmo código PyTorch a rodar em qualquer configuração distribuída.
Mais informações: <https://huggingface.co/docs/accelerate/index>.

- Mostra informações do ambiente:

`accelerate env`

- Cria um arquivo de configuração de forma interativa:

`accelerate config`

- Mostra o custo de memória de GPU estimado para rodar um Modelo de Face aumentado com diferentes tipos de dados:

`accelerate estimate-memory `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome/modelo</span>

- Testa um arquivo Accelerate de configuração:

`accelerate test --config_file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/config.yaml</span>

- Roda um modelo na CPU com Accelerate:

`accelerate launch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/script.py</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">--cpu</span>

- Roda um modelo em multi-GPU com Accelerate, com 2 máquinas:

`accelerate launch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/script.py</span>` --multi_gpu --num_machines 2`
