---
layout: page
title: linux/curlie (français)
description: "Curlie est un frontend pour curl qui ajoute la facilité d'utilisation de httpie."
content_hash: b530d434be4d47617d5324ae247772c5c0c1d6bf
last_modified_at: 2022-12-29
related_topics:
  - title: English version
    url: /en/linux/curlie.html
    icon: bi bi-globe
---
# curlie

Curlie est un frontend pour curl qui ajoute la facilité d'utilisation de httpie.
Plus d'informations : <https://github.com/rs/curlie>.

- Envoie une requête GET :

`curlie `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">httpbin.org/get</span>

- Envoie une requête POST :

`curlie post `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">httpbin.org/post</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name=john</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">age:=25</span>

- Envoie une requête GET avec des paramètres de requête (par ex : `premier_param=5&deuxième_param=true`) :

`curlie get `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">httpbin.org/get</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">premier_param=5</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">second_param=true</span>

- Envoie une requête GET avec un en-tête personnalisé :

`curlie get `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">httpbin.org/get</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">clef-d-en-tête:valeur-d-en-tête</span>
