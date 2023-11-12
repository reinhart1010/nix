---
layout: page
title: common/age (italiano)
description: "Uno strumento semplice, moderno e sicuro per la cifratura di file."
content_hash: dc2ea7a9471bafd83a5eaca6bd267b0eadd8b7ab
last_modified_at: 2023-11-12
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
  - title: Nederlands version
    url: /nl/common/age.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/age.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/age.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># age

Uno strumento semplice, moderno e sicuro per la cifratura di file.
Maggiori informazioni: <https://github.com/FiloSottile/age>.

- Generare un file cifrato che può essere decifrato con una passphrase:

`age --passphrase --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/file_cifrato</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/file_non_cifrato</span>

- Generare una coppia di chiavi, salvando la chiave privata in un file non cifrato e stampando sullo `stdout` la chiave pubblica:

`age-keygen --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/file</span>

- Cifrare un file con una o più chiavi pubbliche inserite come letterali:

`age --recipient `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chiave_pubblica_1</span>` --recipient `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chiave_pubblica_2</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/file_non_cifrato</span>` --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/file_cifrato</span>

- Cifrare un file con una o più chiavi pubbliche specificate in un file di destinatari:

`age --recipients-file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/file_di_destinatari</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/file_non_cifrato</span>` --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/file_cifrato</span>

- Decifrare un file con una passphrase:

`age --decrypt --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/file_decifrato</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/file_cifrato</span>

- Decifrare un file con il file di una chiave privata:

`age --decrypt --identity `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/file_chiave_privata</span>` --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/file_decifrato</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/file_cifrato</span>
