---
layout: page
title: common/ar (italiano)
description: "Crea, modifica ed estrai da archivi (`.a`, `.so`, `.o`)."
content_hash: 939486706c1ff4336cd0dd37c5734a1f726025e6
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/ar.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/ar.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/ar.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/ar.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ar

Crea, modifica ed estrai da archivi (`.a`, `.so`, `.o`).
Maggiori informazioni: <https://manned.org/ar>.

- Estrai tutti i membri da un archivio:

`ar -x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">libfoo.a</span>

- Lista tutti i membri di un archivio:

`ar -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">libfoo.a</span>

- Sostituisci o aggiungi file ad un archvio:

`ar -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">libfoo.a</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">foo.o</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bar.o</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">baz.o</span>

- Inserisci o sostituisci un indice in un archivio (equivalente ad usare `ranlib`):

`ar -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">libfoo.a</span>

- Crea un archivio con dei file creando anche il relativo indice:

`ar -rs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">libfoo.a</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">foo.o</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bar.o</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">baz.o</span>
