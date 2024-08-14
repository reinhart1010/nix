---
layout: page
title: osx/cat (Nederlands)
description: "Print en concateneer bestanden."
content_hash: ac926c3fdb6f520af622f6615de6b688cba745c8
last_modified_at: 2024-08-14
related_topics:
  - title: English version
    url: /en/osx/cat.html
    icon: bi bi-globe
tldri18n_status: 2
---
# cat

Print en concateneer bestanden.
Meer informatie: <https://keith.github.io/xcode-man-pages/cat.1.html>.

- Print de inhoud van een bestand naar `stdout`:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>

- Concateneer meerdere bestanden in een uitvoerbestand:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand1 pad/naar/bestand2 ...</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/uitvoerbestand</span>

- Voeg meerdere bestanden toe aan een uitvoerbestand:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand1 pad/naar/bestand2 ...</span>` >> `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/uitvoerbestand</span>

- Kopieer de inhoud van een bestand naar een uitvoerbestand zonder buffering:

`cat -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/tty12</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/tty13</span>

- Schrijf `stdin` naar een bestand:

`cat - > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>

- Nummer alle uitvoerregels:

`cat -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>

- Toon niet-afdrukbare en witruimtekarakters (met `M-` prefix als niet-ASCII):

`cat -v -t -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>
