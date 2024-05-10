---
layout: page
title: sunos/prctl (polski)
description: "Pobieraj lub ustawiaj kontrolę zasobów uruchomionych procesów, zadań i projektów."
content_hash: f361e54de2cc08ba2e6ec7332ba2864199936959
last_modified_at: 2024-05-10
related_topics:
  - title: English version
    url: /en/sunos/prctl.html
    icon: bi bi-globe
  - title: français version
    url: /fr/sunos/prctl.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/sunos/prctl.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/sunos/prctl.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/sunos/prctl.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/sunos/prctl.html
    icon: bi bi-globe
tldri18n_status: 2
---
# prctl

Pobieraj lub ustawiaj kontrolę zasobów uruchomionych procesów, zadań i projektów.
Więcej informacji: <https://www.unix.com/man-page/sunos/1/prctl>.

- Sprawdź limity procesów i uprawnienia:

`prctl `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pid</span>

- Sprawdź limity procesów i uprawnienia w formacie przetwarzalnym przez maszynę:

`prctl -P `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pid</span>

- Uzyskaj określony limit dla uruchomionego procesu:

`prctl -n process.max-file-descriptor `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pid</span>
