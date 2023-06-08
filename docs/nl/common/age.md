---
layout: page
title: common/age (Nederlands)
description: "Een eenvoudige, moderne en veilige tool voor het versleutelen van bestanden."
content_hash: 61f1deee18fb882a98f249c6750fc7c38df38b16
last_modified_at: 2023-06-08
related_topics:
  - title: Deutsch version
    url: /de/common/age.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/age.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/age.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/age.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/age.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/age.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/age.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># age

Een eenvoudige, moderne en veilige tool voor het versleutelen van bestanden.
Meer informatie: <https://github.com/FiloSottile/age>.

- Genereer een versleuteld bestand dat kan worden ontsleuteld met een wachtwoordzin:

`age --passphrase --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/versleuteld_bestand</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/niet-versleuteld_bestand</span>

- Genereer een sleutelpaar, sla de privésleutel op in een niet-versleuteld bestand en druk de openbare sleutel af naar `stdout`:

`age-keygen --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>

- Versleutel een bestand met een of meer openbare sleutels die als letterlijke waarden worden ingevoerd:

`age --recipient `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">openbare_sleutel_1</span>` --recipient `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">openbare_sleutel_2</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/niet-versleuteld_bestand</span>` --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/versleuteld_bestand</span>

- Versleutel een bestand met een of meer openbare sleutels die zijn opgegeven in het bestand van een ontvanger:

`age --recipients-file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/ontvangers_bestand</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/niet-versleuteld_bestand</span>` --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/versleuteld_bestand</span>

- Decodeer een bestand met een wachtwoordzin:

`age --decrypt --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/gedecodeerd_bestand</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/versleuteld_bestand</span>

- Ontsleutel een bestand met een privésleutelbestand:

`age --decrypt --identity `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/privé_sleutel_bestand</span>` --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/gedecodeerd_bestand</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/versleuteld_bestand</span>
