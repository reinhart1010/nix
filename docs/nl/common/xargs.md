---
layout: page
title: common/xargs (Nederlands)
description: "Voer een commando uit met doorgegeven argumenten van een ander commando, een bestand, etc."
content_hash: 41adb6c4030664da7e2b9b771857e8d3aef8723b
last_modified_at: 2024-08-13
related_topics:
  - title: English version
    url: /en/common/xargs.html
    icon: bi bi-globe
tldri18n_status: 2
---
# xargs

Voer een commando uit met doorgegeven argumenten van een ander commando, een bestand, etc.
De invoer wordt behandeld als een enkel tekstblok en gesplitst in afzonderlijke stukken op spaties, tabbladen, nieuwe regels en einde-van-bestand.
Meer informatie: <https://pubs.opengroup.org/onlinepubs/9699919799/utilities/xargs.html>.

- Voer een commando uit met de invoergegevens als argumenten:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">argumenten_bron</span>` | xargs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commando</span>

- Voer meerdere gekoppelde commando's uit op de invoergegevens:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">argumenten_bron</span>` | xargs sh -c "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commando1</span>` && `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commando2</span>` | `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commando3</span>`"`

- Gzip alle bestanden met een `.log` extensie en profiteer van het voordeel van meerdere threads (`-print0` gebruikt een nul-teken om bestandsnamen te splitsen en `-0` gebruikt het als scheidingsteken):

`find . -name '*.log' -print0 | xargs -0 -P `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">4</span>` -n 1 gzip`

- Voer het commando eenmaal per argument uit:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">argumenten_bron</span>` | xargs -n1 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commando</span>

- Voer het commando één keer uit voor elke invoerregel, waarbij elke plaatsaanduiding (hier gemarkeerd als `_`) wordt vervangen door de invoerregel:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">argumenten_bron</span>` | xargs -I _ `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commando</span>` _ `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">optionele_extra_argumenten</span>

- Parallelle uitvoeringen van maximaal `max-procs` processen tegelijk; de standaard is 1. Als `max-procs` 0 is, zal xargs zoveel mogelijk processen tegelijk uitvoeren:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">argumenten_bron</span>` | xargs -P `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">max-procs</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commando</span>
