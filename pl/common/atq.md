---
layout: page
title: common/atq (polski)
description: "Pokaż oczekujące zadania użytkownika wprowadzone wcześniej przez polecenia `at` lub `batch`."
content_hash: 619b53e3fbfe7b50aadc0d14b8337978f3c3a16b
related_topics:
  - title: English version
    url: /en/common/atq.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/atq.html
    icon: bi bi-globe
---
# atq

Pokaż oczekujące zadania użytkownika wprowadzone wcześniej przez polecenia `at` lub `batch`.
Więcej informacji: <https://man.archlinux.org/man/at.1>.

- Pokaż zaplanowane zadania:

`atq`

- Pokaż zadania z kolejki oznaczonej 'a' (kolejki mają jednoznakowe identyfikatory):

`atq -q `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">a</span>

- Pokaż zadania wszystkich użytkowników (uruchom jako superużytkownik):

`sudo atq`
