---
layout: page
title: common/xxd (italiano)
description: "Mostra la rappresentazione esadecimale (hexdump) di un file binario e viceversa."
content_hash: 0b27f50b74c72a50ca517ed9d087a9ae500aee51
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/xxd.html
    icon: bi bi-globe
tldri18n_status: 2
---
# xxd

Mostra la rappresentazione esadecimale (hexdump) di un file binario e viceversa.
Maggiori informazioni: <https://manned.org/xxd>.

- Creare l'hexdump di un file binario e mostrare l'output:

`xxd `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file_di_input</span>

- Creare l'hexdump di un file binario e salvare il risultato in un file:

`xxd `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file_di_input</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file_di_output</span>

- Mostrare un output in una versione un po' più compatta, dove gli zero consegutivi vengono sostituiti da un asterisco:

`xxd -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file_di_input</span>

- Mostrare l'output in 10 colonne di un ottetto (byte) ciascuna:

`xxd -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file_di_input</span>

- Mostrare l'output solo fino ad una lunghezza massima di 32 bytes:

`xxd -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">32</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file_di_input</span>

- Mostrare l'output in modalità normale, senza spazi tra le colonne:

`xxd -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file_di_input</span>

- Eseguire l'operazione inversa, ovvero da un hexdump creare il binario e salvarlo in un file:

`xxd -r -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file_di_input</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file_di_output</span>
