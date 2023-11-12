---
layout: page
title: common/aws-history (português (Brasil))
description: "Exibe o histórico dos comandos para o AWS CLI (o armazenamento do hisitórico dos comandos do AWS CLI deve estar habilitado)."
content_hash: 6509dc0e0da56f72d365c02ed60f98bffe77721f
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/aws-history.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/aws-history.html
    icon: bi bi-globe
tldri18n_status: 2
---
# aws history

Exibe o histórico dos comandos para o AWS CLI (o armazenamento do hisitórico dos comandos do AWS CLI deve estar habilitado).
Mais informações: <https://docs.aws.amazon.com/cli/latest/reference/history/>.

- Lista histórico dos comandos e seus IDs:

`aws history list`

- Exibe eventos relacionados a um comando específico dado um ID do comando:

`aws history show `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id_do_comando</span>
