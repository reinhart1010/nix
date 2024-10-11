---
layout: page
title: linux/dnf-config-manager (Nederlands)
description: "Beheer DNF-configuratie-opties en repositories op Fedora-gebaseerde systemen."
content_hash: 1e9dd150076b2fe17594bb043f4a27459f6eb65f
last_modified_at: 2024-10-11
related_topics:
  - title: English version
    url: /en/linux/dnf-config-manager.html
    icon: bi bi-globe
tldri18n_status: 2
---
# dnf config-manager

Beheer DNF-configuratie-opties en repositories op Fedora-gebaseerde systemen.
Meer informatie: <https://manned.org/dnf-config-manager>.

- Voeg een repository toe (en schakel deze in) vanaf een URL:

`dnf config-manager --add-repo=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">repository_url</span>

- Print de huidige configuratiewaarden:

`dnf config-manager --dump`

- Schakel een specifieke repository in:

`dnf config-manager --set-enabled `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">repository_id</span>

- Schakel opgegeven repositories uit:

`dnf config-manager --set-disabled `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">repository_id1 repository_id2 ...</span>

- Stel een configuratieoptie in voor een repository:

`dnf config-manager --setopt=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">option</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">value</span>

- Toon hulp:

`dnf config-manager --help-cmd`
