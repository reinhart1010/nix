---
layout: page
title: common/mongo (português (Brasil))
description: "Cliente shell interativo de MongoDB."
content_hash: 550f599cf63192993ebdb69ba3524268a62018fd
last_modified_at: 2024-01-10
related_topics:
  - title: English version
    url: /en/common/mongo.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/mongo.html
    icon: bi bi-globe
tldri18n_status: 2
---
# mongo

Cliente shell interativo de MongoDB.
Mais informações: <https://docs.mongodb.com/manual/reference/program/mongo>.

- Conecta a uma base de dados local na porta padrão (mongodb://localhost:27017):

`mongo`

- Conecta a uma base de dados em um host e porta específicos:

`mongo --host `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>` --port `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">porta</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">base_de_dados</span>

- Autentica usando, na base de dados especificada, o nome de usuário especificado (uma senha será solicitada):

`mongo --host `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>` --port `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">porta</span>` --username `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">usuário</span>` --authenticationDatabase `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">auth_base_de_dados</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">base_de_dados</span>

- Avalia JavaScript na base de dados:

`mongo --eval '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">JSON.stringify(db.foo.findOne())</span>`' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">base_de_dados</span>
