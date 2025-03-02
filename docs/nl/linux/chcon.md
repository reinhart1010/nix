---
layout: page
title: linux/chcon (Nederlands)
description: "Verander SELinux beveiligingscontext van een bestand of bestanden/mappen."
content_hash: 243e7e24e9e01f9b1cd310b06f55f1061bd25ef1
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/linux/chcon.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/chcon.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/linux/chcon.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/chcon.html
    icon: bi bi-globe
tldri18n_status: 2
---
# chcon

Verander SELinux beveiligingscontext van een bestand of bestanden/mappen.
Meer informatie: <https://www.gnu.org/software/coreutils/manual/html_node/chcon-invocation.html>.

- Toon beveiligingscontext van een bestand:

`ls -lZ `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>

- Verander de beveiligingscontext van een doelbestand, door gebruik te maken van een referentiebestand:

`chcon --reference=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">referentiebestand</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">doelbestand</span>

- Verander de volledige SELinux beveiligingscontext van een bestand:

`chcon `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gebruiker</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">rol</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">type</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bereik/niveau</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bestandsnaam</span>

- Verander alleen het gebruikersgedeelte van de SELinux beveiligingscontext:

`chcon -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">user</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bestandsnaam</span>

- Verander alleen het rolgedeelte van de SELinux beveiligingscontext:

`chcon -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">rol</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bestandsnaam</span>

- Verander alleen het typegedeelte van de SELinux beveiligingscontext:

`chcon -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">type</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bestandsnaam</span>

- Verander alleen het bereik/niveaugedeelte van de SELinux beveiligingscontext:

`chcon -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bereik/niveau</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bestandsnaam</span>
