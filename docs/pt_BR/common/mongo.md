---
layout: page
title: common/mongo (português (Brasil))
description: "Cliente shell interativo de MongoDB."
content_hash: a614248062cc622aeab44a2f6723bc9a85790562
related_topics:
  - title: English version
    url: /en/common/mongo.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/mongo.html
    icon: bi bi-globe
---
# mongo

Cliente shell interativo de MongoDB.
Mais informações: <https://docs.mongodb.com/manual/reference/program/mongo>.

- Conectar a uma base de dados:

`mongo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">base_de_dados</span>

- Conectar a uma base de dados em um host e porta específicos:

`mongo --host `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>` --port `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">porta</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">base_de_dados</span>

- Conectar a uma base de dados com um usuário específico, uma senha será pedida ao usuário:

`mongo --username `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">usuário</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">base_de_dados</span>` --password`

- Avaliar JavaScript na base de dados:

`mongo --eval '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">JSON.stringify(db.foo.findOne())</span>`' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">base_de_dados</span>
