---
layout: page
title: linux/libtoolize (Nederlands)
description: "Een `autotools` tool om een pakket voor te bereiden voor het gebruik van `libtool`."
content_hash: 47f94bb2b1512423f1e830cdc5e59e9c1a2237a7
last_modified_at: 2024-06-26
related_topics:
  - title: English version
    url: /en/linux/libtoolize.html
    icon: bi bi-globe
tldri18n_status: 2
---
# libtoolize

Een `autotools` tool om een pakket voor te bereiden voor het gebruik van `libtool`.
Het voert verschillende taken uit, waaronder het genereren van de benodigde bestanden en directories om `libtool` naadloos in een project te integreren.
Meer informatie: <https://www.gnu.org/software/libtool/manual/libtool.html#Invoking-libtoolize>.

- Initialiseer een project voor `libtool` door de benodigde bestanden te kopiëren (symbolische links vermijden) en bestaande bestanden indien nodig te overschrijven:

`libtoolize --copy --force`
