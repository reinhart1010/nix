---
layout: page
title: common/mongo (français)
description: "Client shell pour MongoDB."
content_hash: 972627612c41c11d9fd1be647ebdf11edd3588f6
last_modified_at: 2023-12-28
related_topics:
  - title: English version
    url: /en/common/mongo.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/mongo.html
    icon: bi bi-globe
tldri18n_status: 2
---
# mongo

Client shell pour MongoDB.
Plus d'informations : <https://docs.mongodb.com/manual/reference/program/mongo>.

- Connecte à une base de données (database) sur un hôte (host) distant et un port donné :

`mongo --host `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hôte</span>` --port `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">port</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_de_la_base_de_données</span>

- Évalue une expression JavaScript sur une base de données (database) :

`mongo --eval '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">JSON.stringify(db.foo.findOne())</span>`' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_de_la_base_de_données</span>
