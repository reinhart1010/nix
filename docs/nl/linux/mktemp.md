---
layout: page
title: linux/mktemp (Nederlands)
description: "Maak een tijdelijk bestand of een tijdelijke map aan."
content_hash: c438e0c8141b876ff52b315fe002a31e86eed72d
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/linux/mktemp.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/mktemp.html
    icon: bi bi-globe
tldri18n_status: 2
---
# mktemp

Maak een tijdelijk bestand of een tijdelijke map aan.
Meer informatie: <https://www.gnu.org/software/coreutils/manual/html_node/mktemp-invocation.html>.

- Maak een leeg tijdelijk bestand en toon het absolute pad:

`mktemp`

- Gebruik een aangepaste map (standaard is `$TMPDIR`, of `/tmp`):

`mktemp --tmpdir=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/pad/naar/tempdir</span>

- Gebruik een aangepast pad-sjabloon (`X`en worden vervangen door willekeurige alfanumerieke tekens):

`mktemp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/tmp/voorbeeld.XXXXXXXX</span>

- Gebruik een aangepast bestandsnaam-sjabloon:

`mktemp -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">voorbeeld.XXXXXXXX</span>

- Maak een leeg tijdelijk bestand met de opgegeven extensie en toon het absolute pad:

`mktemp --suffix `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">.ext</span>

- Maak een lege tijdelijke map aan en toon het absolute pad:

`mktemp --directory`
