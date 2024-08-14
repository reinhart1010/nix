---
layout: page
title: common/zip (Nederlands)
description: "Verpak en comprimeer (archiveer) bestanden in een Zip-archief."
content_hash: 91c3bf0457b88ebb95d719d1a0ece6cb618de805
last_modified_at: 2024-08-14
related_topics:
  - title: English version
    url: /en/common/zip.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/zip.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/zip.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/zip.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/zip.html
    icon: bi bi-globe
tldri18n_status: 2
---
# zip

Verpak en comprimeer (archiveer) bestanden in een Zip-archief.
Bekijk ook: `unzip`.
Meer informatie: <https://manned.org/zip>.

- Voeg bestanden/directories toe aan een specifiek archief ([r]ecursief):

`zip -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/gecomprimeerd.zip</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand_of_directory1 pad/naar/bestand_of_directory2 ...</span>

- Verwijder bestanden/directories uit een specifiek archief ([d]elete):

`zip -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/gecomprimeerd.zip</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand_of_directory1 pad/naar/bestand_of_directory2 ...</span>

- Archiveer bestanden/directories waarbij opgegeven bestanden worden uitgesloten:

`zip -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/gecomprimeerd.zip</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand_of_directory1 pad/naar/bestand_of_directory2 ...</span>` -x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/uitgesloten_bestanden_of_directories</span>

- Archiveer bestanden/directories met een specifieke compressieniveau (`0` - het laagste, `9` - het hoogste):

`zip -r -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0..9</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/gecomprimeerd.zip</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand_of_directory1 pad/naar/bestand_of_directory2 ...</span>

- Maak een [e]ncrypted archief met een specifiek wachtwoord:

`zip -r -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/gecomprimeerd.zip</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand_of_directory1 pad/naar/bestand_of_directory2 ...</span>

- Archiveer bestanden/directories in een multipart [s]plit Zip-archief (bijv. 3 GB delen):

`zip -r -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3g</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/gecomprimeerd.zip</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand_of_directory1 pad/naar/bestand_of_directory2 ...</span>

- Print de inhoud van een specifiek archief:

`zip -sf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/gecomprimeerd.zip</span>
