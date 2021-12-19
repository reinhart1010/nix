---
layout: page
title: common/mongo (français)
description: "Client shell pour MongoDB."
content_hash: 819a10ab46e52f4fb09f69d9b4c1d932d9fc28b9
related_topics:
  - title: English version
    url: /en/common/mongo.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/mongo.html
    icon: bi bi-globe
---
# mongo

Client shell pour MongoDB.
Plus d'informations : <https://docs.mongodb.com/manual/reference/program/mongo>.

- Connecte à une base de données (database) :

`mongo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_de_la_base_de_données</span>

- Connecte à une base de données (database) sur un hôte (host) distant et un port donné :

`mongo --host `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hôte</span>` --port `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">port</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_de_la_base_de_données</span>

- Connecte à une base de données (database) avec un nom d'utilisateur (username); L'utilisateur sera invité à saisir son mot de passe :

`mongo --username `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_d'utilisateur</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_de_la_base_de_données</span>` --password`

- Évalue une expression JavaScript sur une base de données (database) :

`mongo --eval '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">JSON.stringify(db.foo.findOne())</span>`' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_de_la_base_de_données</span>
