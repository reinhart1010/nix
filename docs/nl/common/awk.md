---
layout: page
title: common/awk (Nederlands)
description: "Een veelzijdige programmeertaal voor het werken met bestanden."
content_hash: b0c1bcc650cf69fca8fa740012f1d765c6246d41
last_modified_at: 2024-08-26
related_topics:
  - title: English version
    url: /en/common/awk.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/awk.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/awk.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/awk.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/awk.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/awk.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/awk.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/awk.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/awk.html
    icon: bi bi-globe
tldri18n_status: 2
---
# awk

Een veelzijdige programmeertaal voor het werken met bestanden.
Meer informatie: <https://github.com/onetrueawk/awk>.

- Toon de vijfde kolom (a.k.a. veld) in een spatie-gescheiden bestand:

`awk '{print $5}' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>

- Toon de tweede kolom van de regels die "foo" bevatten in een spatie-gescheiden bestand:

`awk '/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">foo</span>`/ {print $2}' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>

- Toon de laatste kolom van iedere regel in een bestand en maak gebruik van een komma (in plaats van een spatie) als veld scheider:

`awk -F ',' '{print $NF}' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>

- Tel de waarden in de eerste kolom van een bestand op en toon het totaal:

`awk '{s+=$1} END {print s}' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>

- Toon iedere derde regel startend vanaf de eerste regel:

`awk 'NR%3==1' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>

- Toon verschillende waardes gebaseerd op condities:

`awk '{if ($1 == "foo") print "Exact match foo"; else if ($1 ~ "bar") print "Partial match bar"; else print "Baz"}' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>

- Toon alle regels waarbij de waarde van de 10e kolom gelijk is aan de gespecificeerde waarde:

`awk '($10 == `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">value</span>`)'`

- Print een tabel van gebruikers met UID >= 1000 met header en opgemaakte uitvoer, gebruikmakend van een dubbele punt als scheidingsteken (`%-20s` betekent: 20 links uitgelijnde tekens, `%6s` betekent: 6 rechts uitgelijnde tekens):

`awk 'BEGIN {FS=":"; printf "%-20s %6s %25s\n", "Name", "UID", "Shell"} $3 >= 1000 {printf "%-20s %6d %25s\n", $1, $3, $7}' /etc/passwd`
