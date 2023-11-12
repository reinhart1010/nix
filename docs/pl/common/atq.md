---
layout: page
title: common/atq (polski)
description: "Pokaż oczekujące zadania użytkownika wprowadzone wcześniej przez polecenia `at` lub `batch`."
content_hash: 873fbdd480a7eaccb3da642a8c8d41b568d19cfa
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/atq.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/atq.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/atq.html
    icon: bi bi-globe
tldri18n_status: 2
---
# atq

Pokaż oczekujące zadania użytkownika wprowadzone wcześniej przez polecenia `at` lub `batch`.
Więcej informacji: <https://manned.org/atq>.

- Pokaż zaplanowane zadania:

`atq`

- Pokaż zadania z kolejki oznaczonej 'a' (kolejki mają jednoznakowe identyfikatory):

`atq -q `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">a</span>

- Pokaż zadania wszystkich użytkowników (uruchom jako superużytkownik):

`sudo atq`
