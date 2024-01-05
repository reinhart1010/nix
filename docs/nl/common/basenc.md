---
layout: page
title: common/basenc (Nederlands)
description: "Encodeer of decodeer een bestand of `stdin` door gebruik te maken van een specifieke encoding naar `stdout`."
content_hash: ad06636c0065038fa695ddfb9f096563ead1902c
last_modified_at: 2024-01-05
related_topics:
  - title: English version
    url: /en/common/basenc.html
    icon: bi bi-globe
tldri18n_status: 2
---
# basenc

Encodeer of decodeer een bestand of `stdin` door gebruik te maken van een specifieke encoding naar `stdout`.
Meer informatie: <https://www.gnu.org/software/coreutils/basenc>.

- Encodeer een bestand met base64 encoding:

`basenc --base64 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>

- Decodeer een bestand met base64 encoding:

`basenc --decode --base64 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>

- Encodeer `stdin` met base32 encoding met 42 kolommen:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>` | basenc --base32 -w42`

- Encodeer `stdin` met base32 encoding:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>` | basenc --base32`
