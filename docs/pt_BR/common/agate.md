---
layout: page
title: common/agate (português (Brasil))
description: "Um simples servidor para o protocolo de internet Gemini."
content_hash: 702c018ef5582af17652c16408b8182297f563da
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/agate.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/agate.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/agate.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/agate.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/agate.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/agate.html
    icon: bi bi-globe
tldri18n_status: 2
---
# agate

Um simples servidor para o protocolo de internet Gemini.
Mais informações: <https://github.com/mbrubeck/agate>.

- Executa e gera uma chave privada e um certificado:

`agate --content `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/conteudo/</span>` --addr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">[::]:1965</span>` --addr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0.0.0.0:1965</span>` --hostname `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>` --lang `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">en-US</span>

- Executa o servidor:

`agate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo</span>

- Exibe opções de ajuda:

`agate -h`
