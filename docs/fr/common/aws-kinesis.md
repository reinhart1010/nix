---
layout: page
title: common/aws-kinesis (français)
description: "CLI officiel d'AWS pour les services de streaming d'Amazon Kinesis."
content_hash: 608cfb48d5fd3478ad17b3bdc7deaabea8833a90
related_topics:
  - title: Deutsch version
    url: /de/common/aws-kinesis.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/aws-kinesis.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># aws kinesis

CLI officiel d'AWS pour les services de streaming d'Amazon Kinesis.
Plus d'informations : <https://docs.aws.amazon.com/cli/latest/reference/kinesis/index.html#cli-aws-kinesis>.

- Affiche tous les streams du compte :

`aws kinesis list-streams`

- Écris une entrée dans le stream Kinesis :

`aws kinesis put-record --stream-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom</span>` --partition-key `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">clé</span>` --data `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">message_encodé_en_base64</span>

- Écris une entrée dans le stream Kinesis avec un encodage base64 inline :

`aws kinesis put-record --stream-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom</span>` --partition-key `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">clé</span>` --data "$( echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mon message</span>`" | base64 )"`

- Liste tous les fragments disponible dans un stream :

`aws kinesis list-shards --stream-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom</span>

- Récupère un fragment pour lire depuis le plus vieux message dans la stream de ce dernier :

`aws kinesis get-shard-iterator --shard-iterator-type TRIM_HORIZON --stream-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom</span>` --shard-id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id</span>

- Lis les entrées d'un fragment en utilisant un itérateur de fragment :

`aws kinesis get-records --shard-iterator `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">itérateur</span>
