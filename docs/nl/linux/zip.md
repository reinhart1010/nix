---
layout: page
title: linux/zip (Nederlands)
description: "Verpak en comprimeer (archiveer) bestanden in een Zip-archief."
content_hash: 5ebd0bc3476de6b035bf690cab0a7db57849b850
last_modified_at: 2024-08-14
related_topics:
  - title: English version
    url: /en/linux/zip.html
    icon: bi bi-globe
tldri18n_status: 2
---
# zip

Verpak en comprimeer (archiveer) bestanden in een Zip-archief.
Bekijk ook: `unzip`.
Meer informatie: <https://manned.org/zip>.

- Voeg bestanden/directories toe aan een specifiek archief:

`zip -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/gecomprimeerd.zip</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand_of_directory1 pad/naar/bestand_of_directory2 ...</span>

- Verwijder bestanden/directories uit een specifiek archief:

`zip --delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/gecomprimeerd.zip</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand_of_directory1 pad/naar/bestand_of_directory2 ...</span>

- Archiveer bestanden/directories waarbij opgegeven bestanden worden uitgesloten:

`zip `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/gecomprimeerd.zip</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand_of_directory1 pad/naar/bestand_of_directory2 ...</span>` --exclude `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/uitgesloten_bestanden_of_directories</span>

- Archiveer bestanden/directories met een specifieke compressieniveau (`0` - het laagste, `9` - het hoogste):

`zip -r -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0..9</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/gecomprimeerd.zip</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand_of_directory1 pad/naar/bestand_of_directory2 ...</span>

- Maak een versleuteld archief met een specifiek wachtwoord:

`zip -r --encrypt `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/gecomprimeerd.zip</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand_of_directory1 pad/naar/bestand_of_directory2 ...</span>

- Archiveer bestanden/directories in een multipart [s]plit Zip-archief (bijv. 3 GB delen):

`zip -r -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3g</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/gecomprimeerd.zip</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand_of_directory1 pad/naar/bestand_of_directory2 ...</span>

- Toon de inhoud van een specifiek archief:

`zip -sf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/gecomprimeerd.zip</span>
