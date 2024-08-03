---
layout: page
title: common/xargs (Nederlands)
description: "Voer een commando uit met doorgegeven argumenten van een ander commando, een bestand, etc."
content_hash: 928003ffe231eb58d2ee515a4d705fa5627ce48e
last_modified_at: 2024-08-03
related_topics:
  - title: English version
    url: /en/common/xargs.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># xargs

Voer een commando uit met doorgegeven argumenten van een ander commando, een bestand, etc.
De invoer wordt behandeld als een enkel tekstblok en gesplitst in afzonderlijke stukken op spaties, tabbladen, nieuwe regels en einde-van-bestand.
Meer informatie: <https://pubs.opengroup.org/onlinepubs/9699919799/utilities/xargs.html>.

- Voer een commando uit met de invoergegevens als argumenten:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">argumenten_bron</span>` | xargs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commando</span>

- Voer meerdere gekoppelde commando's uit op de invoergegevens:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">argumenten_bron</span>` | xargs sh -c "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commando1</span>` && `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commando2</span>` | `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commando3</span>`"`

- Verwijder alle bestanden met een `.backup` extensie (`-print0` gebruikt een nul-teken om bestandsnamen te splitsen en `-0` gebruikt het als scheidingsteken):

`find . -name '*.backup' -print0 | xargs -0 rm -v`

- Voer het commando één keer uit voor elke invoerregel, waarbij elke plaatsaanduiding (hier gemarkeerd als `_`) wordt vervangen door de invoerregel:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">argumenten_bron</span>` | xargs -I _ `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commando</span>` _ `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">optionele_extra_argumenten</span>

- Parallelle uitvoeringen van maximaal `max-procs` processen tegelijk; de standaard is 1. Als `max-procs` 0 is, zal xargs zoveel mogelijk processen tegelijk uitvoeren:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">argumenten_bron</span>` | xargs -P `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">max-procs</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commando</span>
