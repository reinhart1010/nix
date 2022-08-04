---
layout: page
title: common/csvformat (italiano)
description: "Converti un file CSV in un formato di output personalizzato."
content_hash: 1d6780541bc357e0075b7f89e5be508bfbb232bd
related_topics:
  - title: English version
    url: /en/common/csvformat.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/csvformat.html
    icon: bi bi-globe
---
# csvformat

Converti un file CSV in un formato di output personalizzato.
Incluso in csvkit.
Maggiori informazioni: <https://csvkit.readthedocs.io/en/latest/scripts/csvformat.html>.

- Converti in un file delimitato da tab (TSV):

`csvformat -T `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dati.csv</span>

- Converti i delimitatori in un carattere personalizzato:

`csvformat -D "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">carattere_personalizzato</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dati.csv</span>

- Converti caratteri newline a carriage return (^M) + newline:

`csvformat -M "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">\r\n</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dati.csv</span>

- Minimizza l'utilizzo delle virgolette:

`csvformat -U 0 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dati.csv</span>

- Massimizza l'utilizzo delle virgolette:

`csvformat -U 1 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dati.csv</span>
