---
layout: page
title: osx/base64 (italiano)
description: "Codifica e decodifica utilizzando la rappresentazione in base64."
content_hash: ddf666b7c9559c8b030528c5eb4a2562449788b7
last_modified_at: 2023-07-03
related_topics:
  - title: English version
    url: /en/osx/base64.html
    icon: bi bi-globe
  - title: español version
    url: /es/osx/base64.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/osx/base64.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/base64.html
    icon: bi bi-globe
---
# base64

Codifica e decodifica utilizzando la rappresentazione in base64.
Maggiori informazioni: <https://www.unix.com/man-page/osx/1/base64/>.

- Codifica un file:

`base64 -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file_da_codificare</span>

- Decodifica un file:

`base64 --decode -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file_da_decodificare</span>

- Codifica da `stdin`:

`echo -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">testo_da_codificare</span>` | base64`

- Decodifica da `stdin`:

`echo -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">testo_da_decodificare</span>` | base64 --decode`
