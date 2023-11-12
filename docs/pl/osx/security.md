---
layout: page
title: osx/security (polski)
description: "Administruj pękami kluczy, kluczami, certyfikatami oraz framework'iem Security."
content_hash: b55b8b8bef248795db1f40da6eee5e7d2464fa6a
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/osx/security.html
    icon: bi bi-globe
tldri18n_status: 2
---
# security

Administruj pękami kluczy, kluczami, certyfikatami oraz framework'iem Security.
Więcej informacji: <https://ss64.com/osx/security.html>.

- Wypisz wszystkie dostępne pęki kluczy:

`security list-keychains`

- Usuń zadany pęk kluczy:

`security delete-keychain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/pliku.keychain</span>

- Utwórz pęk kluczy:

`security create-keychain -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hasło</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/pliku.keychain</span>

- Ustaw certyfikat który ma być używany przy stronie internetowej lub [s]erwisie używając nazwy własnej (ta komenda nie powiedzie się gdy więcej niż jeden certyfikat ma taką samą nazwę własną):

`security set-identity-preference -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">URL|hostname|serwis</span>` -c "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nazwa_własna</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/pliku.keychain</span>

- Dodaj certyfikat z pliku do pęku [k]luczy (Jeżeli parametr -k nie został podany, domyślny pęk kluczy zostanie wykorzystany):

`security add-certificates -k `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">plik.keychain</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/certyfikatu.keychain.pem</span>

- Dodaj certyfikat CA do ustawień zaufania dla każdego użytkownika:

`security add-trusted-cert -k `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/pęku_kluczy_użytkownika.keychain-db</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/certyfikatu_ca.pem</span>

- Usuń certyfikat CA z ustawień zaufania dla każdego użytkownika:

`security remove-trusted-cert `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ściieżka/do/certyfikatu_ca.pem</span>
