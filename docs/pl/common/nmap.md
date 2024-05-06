---
layout: page
title: common/nmap (polski)
description: "Narzędzie do enumeracji sieci oraz skanowania portów."
content_hash: de888bb6ac91d23e1d9e6f5849ca6e80219578b1
last_modified_at: 2024-05-06
related_topics:
  - title: Deutsch version
    url: /de/common/nmap.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/nmap.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/nmap.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/nmap.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/nmap.html
    icon: bi bi-globe
tldri18n_status: 2
---
# nmap

Narzędzie do enumeracji sieci oraz skanowania portów.
Niektóre funkcję są tylko aktywne gdy Nmap uruchamiany jest z przywilejami root'a.
Więcej informacji: <https://nmap.org/book/man.html>.

- Sprawdź czy host odpowiada na skanowanie oraz zgadnij system operacyjny:

`nmap -O `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip_lub_nazwa_hosta</span>

- Sprawdź czy podane hosty odpowiadają na skanowanie i zgadnij ich nazwy:

`sudo nmap -sn `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip_lub_nazwa_hosta</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">opcjonalny_kolejny_adres_ip</span>

- Poza tym, uruchom domyśle skrypty, wykrywanie działających serwisów, OS fingerprinting oraz komendę traceroute:

`nmap -A `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">adres_lub_adresy_ip</span>

- Skanuj podaną listę portów (użyj '-p-' dla wszystkich portów od 1 do 65535):

`nmap -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">port1,port2,...,portN</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">adres_lub_adresy_ip</span>

- Przeprowadź wykrywanie serwisów i ich wersji dla 1000 najczęstrzych portów używając domyślich skryptów NSE; Zapisz rezultat ('-oN') do pliku wyjściowego:

`nmap -sC -sV -oN `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">top-1000-ports.txt</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">adres_lub_adresy_ip</span>

- Skanuj cel lub cele używając skryptów NSE 'default and safe':

`nmap --script "default and safe" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">adres_lub_adresy_ip</span>

- Skanuj serwer webowy uruchomiony na standardowych portach 80 i 443 używając wszystkich dostępnych skryptów NSE 'http-*':

`nmap --script "http-*" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">adres_lub_adresy_ip</span>` -p 80,443`

- Wykonaj skryty i bardzo wolny skan ('-T0') próbując uniknąć wykrycia przez IDS/IPS i użyj adresu IP wabika ('-D'):

`nmap -T0 -D `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">adres_ip_wabika1,adres_ip_wabika2,...,adres_ip_wabikaN</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">adres_lub_adresy_ip</span>
