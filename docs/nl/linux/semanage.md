---
layout: page
title: linux/semanage (Nederlands)
description: "SELinux persistent beleid beheertool."
content_hash: 5102399c0e883b5809fc3f26510965d4d8bcbb64
last_modified_at: 2024-06-25
related_topics:
  - title: English version
    url: /en/linux/semanage.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/semanage.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># semanage

SELinux persistent beleid beheertool.
Sommige subcommando's zoals `boolean`, `fcontext`, `port`, etc. hebben hun eigen gebruiksdocumentatie.
Meer informatie: <https://manned.org/semanage>.

- Stel een SELinux-boolean in of uit. Booleans stellen de beheerder in staat om aan te passen hoe beleidsregels invloed hebben op ingesloten procestypes (ook wel domeinen genoemd):

`sudo semanage boolean `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-m|--modify</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-1|--on|-0|--off</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">haproxy_connect_any</span>

- Voeg een door de gebruiker gedefinieerde bestandscontextlabelregel toe. Bestandscontexten definiëren welke bestanden ingesloten domeinen mogen openen:

`sudo semanage fcontext `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-a|--add</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-t|--type</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">samba_share_t</span>` '/mnt/share(/.*)?'`

- Voeg een door de gebruiker gedefinieerde poortlabelregel toe. Poortlabels definiëren op welke poorten ingesloten domeinen mogen luisteren:

`sudo semanage port `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-a|--add</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-t|--type</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ssh_port_t</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-p|--proto</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tcp</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">22000</span>

- Stel de permissieve modus in of uit voor een ingesloten domein. Per-domein permissieve modus biedt meer gedetailleerde controle vergeleken met `setenforce`:

`sudo semanage permissive `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-a|--add|-d|--delete</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">httpd_t</span>

- Exporteer lokale aanpassingen in de standaardopslag:

`sudo semanage export `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-f|--output_file</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>

- Importeer een bestand gegenereerd door `semanage export` in lokale aanpassingen (VOORZICHTIG: kan huidige aanpassingen verwijderen!):

`sudo semanage import `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-f|--input_file</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>
