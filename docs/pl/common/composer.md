---
layout: page
title: common/composer (polski)
description: "Menadżer pakietów dla projektów PHP."
content_hash: 311d19d3006fdfc8680e84ca12d20e50f36aa3a2
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/composer.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/composer.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/composer.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/composer.html
    icon: bi bi-globe
tldri18n_status: 2
---
# composer

Menadżer pakietów dla projektów PHP.
Więcej informacji: <https://getcomposer.org/>.

- Interaktywnie utwórz plik `composer.json`:

`composer init`

- Dodaj pakiet do zależności tego projektu, dodając wpis do `composer.json`:

`composer require `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">użytkownik/pakiet</span>

- Zainstaluj wszystkie zależności z projektowego `composer.json` i utwórz `composer.lock`:

`composer install`

- Odinstaluj pakiet z tego projektu, usuwając go jako zależność z `composer.json` i `composer.lock`:

`composer remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">użytkownik/pakiet</span>

- Zaktualizuj wszystkie pakiety z projektowego `composer.json` i zanotuj nową wersję w `composer.lock`:

`composer update`

- Zaktualizuj tylko `composer.lock` po ręcznej aktualizacji `composer.json`:

`composer update --lock`

- Dowiedz się więcej o powodach dlaczego zależność nie może zostać zainstalowana:

`composer why-not `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">użytkownik/pakiet</span>

- Zaktualizuj narzędzie composer do najnowszej wersji:

`composer self-update`
