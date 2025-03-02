---
layout: page
title: common/truncate (Nederlands)
description: "Verkort of verleng de grootte van een bestand naar de opgegeven grootte."
content_hash: 6901343ccc27be73252fa5f4ba5b2151ae4122dc
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/common/truncate.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/truncate.html
    icon: bi bi-globe
tldri18n_status: 2
---
# truncate

Verkort of verleng de grootte van een bestand naar de opgegeven grootte.
Meer informatie: <https://www.gnu.org/software/coreutils/manual/html_node/truncate-invocation.html>.

- Stel een grootte van 10 GB in voor een bestaand bestand, of maak een nieuw bestand met de opgegeven grootte:

`truncate --size 10G `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>

- Verleng de bestandsgrootte met 50 MiB, vul met gaten (die lezen als null bytes):

`truncate --size +50M `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>

- Verkort het bestand met 2 GiB door gegevens van het einde van het bestand te verwijderen:

`truncate --size -2G `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>

- Leeg de inhoud van het bestand:

`truncate --size 0 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>

- Leeg de inhoud van het bestand, maar maak het bestand niet aan als het niet bestaat:

`truncate --no-create --size 0 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>
