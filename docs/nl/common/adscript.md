---
layout: page
title: common/adscript (Nederlands)
description: "Compiler voor Adscript-bestanden."
content_hash: e80ce2b6169c1a333924ea232d79292512e0f4fc
last_modified_at: 2024-06-03
related_topics:
  - title: Deutsch version
    url: /de/common/adscript.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/adscript.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/adscript.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/adscript.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/adscript.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/adscript.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/adscript.html
    icon: bi bi-globe
tldri18n_status: 2
---
# adscript

Compiler voor Adscript-bestanden.
Meer informatie: <https://github.com/Amplus2/Adscript>.

- Compileer een bestand naar een objectbestand:

`adscript --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand.o</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/invoer_bestand.adscript</span>

- Compileer en koppel een bestand aan een zelfstandig uitvoerbaar bestand:

`adscript --executable --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/invoer_bestand.adscript</span>

- Compileer een bestand naar LLVM IR in plaats van native machinecode:

`adscript --llvm-ir --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand.ll</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/invoer_bestand.adscript</span>

- Cross-compileer een bestand naar een objectbestand voor een buitenlandse CPU-architectuur of besturingssysteem:

`adscript --target-triple `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">i386-linux-elf</span>` --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand.o</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/invoer_bestand.adscript</span>
