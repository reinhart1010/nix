---
layout: page
title: windows/scoop-bucket (polski)
description: "Zarządzaj bucketami: repozytoriami Git zawierającymi pliki, które opisują sposób instalacji aplikacji przez Scoop."
content_hash: c95772943e8789d23521f72cc3af0fc37a8dbd28
last_modified_at: 2025-03-02
related_topics:
  - title: Deutsch version
    url: /de/windows/scoop-bucket.html
    icon: bi bi-globe
  - title: English version
    url: /en/windows/scoop-bucket.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/windows/scoop-bucket.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/windows/scoop-bucket.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/scoop-bucket.html
    icon: bi bi-globe
tldri18n_status: 2
---
# scoop bucket

Zarządzaj bucketami: repozytoriami Git zawierającymi pliki, które opisują sposób instalacji aplikacji przez Scoop.
Jeśli Scoop nie zna lokalizacji bucketa, należy określić lokalizację jego repozytorium.
Więcej informacji: <https://github.com/lukesampson/scoop/wiki/Buckets>.

- Wyświetl wszystkie aktualnie używane buckety:

`scoop bucket list`

- Wyświetl wszystkie znane buckety:

`scoop bucket known`

- Dodaj znany bucket według jego nazwy:

`scoop bucket add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nazwa</span>

- Dodaj nieznany bucket według jego nazwy i adresu URL repozytorium Git:

`scoop bucket add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nazwa</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com/repository.git</span>

- Usuń bucket według jego nazwy:

`scoop bucket rm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nazwa</span>
