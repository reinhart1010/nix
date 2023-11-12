---
layout: page
title: common/age-keygen (Nederlands)
description: "Genereer `age` sleutelparen."
content_hash: 38b3de045f424227f7fa73ecd96ec2b18c3e9b9d
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/age-keygen.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/age-keygen.html
    icon: bi bi-globe
tldri18n_status: 2
---
# age-keygen

Genereer `age` sleutelparen.
Bekijk `age` hoe je bestanden kan versleutelen/decoderen.
Meer informatie: <https://manned.org/age-keygen>.

- Genereer een sleutelpaar, sla de privésleutel op in een niet-versleuteld bestand en druk de openbare sleutel af naar `stdout`:

`age-keygen --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>

- Converteer een identity naar een recipient een print de publieke sleutel naar `stdout`:

`age-keygen -y `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>
