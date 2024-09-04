---
layout: page
title: common/atq (polski)
description: "Pokaż zadania zaplanowane przez polecenia `at` lub `batch`."
content_hash: 8f7f564f80ef4f76959195176a94d15abc0acea7
last_modified_at: 2024-09-04
related_topics:
  - title: English version
    url: /en/common/atq.html
    icon: bi bi-globe
  - title: فارسی version
    url: /fa/common/atq.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/atq.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/atq.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/atq.html
    icon: bi bi-globe
tldri18n_status: 2
---
# atq

Pokaż zadania zaplanowane przez polecenia `at` lub `batch`.
Więcej informacji: <https://manned.org/atq>.

- Pokaż zaplanowane zadania bieżącego użytkownika:

`atq`

- Pokaż zadania z kolejki 'a' (kolejki mają jednoznakowe nazwy):

`atq -q `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">a</span>

- Pokaż zadania wszystkich użytkowników (uruchom jako superużytkownik):

`sudo atq`
