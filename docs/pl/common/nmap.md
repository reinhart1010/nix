---
layout: page
title: common/nmap (polski)
description: "Narzędzie do eksploracji sieci oraz skaner bezpieczeństwa/portów."
content_hash: 94f372723995879aa051c66db855868033078b48
last_modified_at: 2024-08-18
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

Narzędzie do eksploracji sieci oraz skaner bezpieczeństwa/portów.
Niektóre funkcje (np. skan SYN) aktywują się tylko gdy `nmap` jest uruchamiany z przywilejami root'a.
Więcej informacji: <https://nmap.org/book/man.html>.

- Skanuj 1000 najpopularniejszych portów zdalnego hosta z różnymi poziomami szczegółowości ([v]erbosity):

`nmap -v`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1|2|3</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip_lub_nazwa_hosta</span>

- Wykonaj bardzo agresywnie ping sweep w całej podsieci lub na poszczególnych hostach:

`nmap -T5 -sn `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">192.168.0.0/24|ip_lub_nazwa_hosta1,ip_lub_nazwa_hosta2,...</span>

- Włącz wykrywanie systemu operacyjnego, wykrywanie wersji, skanowanie skryptów i traceroute hostów z pliku:

`sudo nmap -A -iL `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/pliku.txt</span>

- Skanuj podaną listę portów (użyj `-p-` dla wszystkich portów od 1 do 65535):

`nmap -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">port1,port2,...</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip_lub_host1,ip_lub_host2,...</span>

- Przeprowadź wykrywanie usług i wersji dla 1000 najpopularniejszych portów używając domyślnych skryptów NSE, zapisując wynik (`-oA`) do plików wyjściowych:

`nmap -sC -sV -oA `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">top-1000-ports</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip_lub_host1,ip_lub_host2,...</span>

- Skanuj cel(e) ostrożnie używając skryptów NSE `default and safe`:

`nmap --script "default and safe" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip_lub_host1,ip_lub_host2,...</span>

- Skanuj w poszukiwaniu serwerów internetowych działających na standardowych portach 80 i 443 przy użyciu wszystkich dostępnych skryptów NSE `http-*`:

`nmap --script "http-*" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip_lub_host1,ip_lub_host2,...</span>` -p 80,443`

- Spróbuj uniknąć wykrycia przez IDS/IPS, używając bardzo powolnego skanowania (`-T0`), fałszywych adresów źródłowych - wabików (`-D`), [f]ragmentowanych pakietów, losowych danych i innych metod:

`sudo nmap -T0 -D `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip_wabika1,ip_wabika2,...</span>` --source-port `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">53</span>` -f --data-length `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">16</span>` -Pn `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip_lub_host</span>
