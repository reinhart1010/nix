---
layout: page
title: linux/secon (Nederlands)
description: "Krijg de SELinux-beveiligingscontext van een bestand, PID, huidige uitvoeringscontext of een contextspecificatie."
content_hash: 18b33b1d4850c115efd61662898e1e7785fabc8f
last_modified_at: 2024-09-19
related_topics:
  - title: English version
    url: /en/linux/secon.html
    icon: bi bi-globe
tldri18n_status: 2
---
# secon

Krijg de SELinux-beveiligingscontext van een bestand, PID, huidige uitvoeringscontext of een contextspecificatie.
Zie ook: `semanage`, `runcon`, `chcon`.
Meer informatie: <https://manned.org/secon>.

- Krijg de beveiligingscontext van de huidige uitvoeringscontext:

`secon`

- Krijg de huidige beveiligingscontext van een proces:

`secon --pid `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1</span>

- Krijg de huidige beveiligingscontext van een bestand, waarbij alle tussenliggende symlinks worden opgelost:

`secon --file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand_of_map</span>

- Krijg de huidige beveiligingscontext van een symlink zelf (d.w.z. niet oplossen):

`secon --link `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/symlink</span>

- Parse en leg een contextspecificatie uit:

`secon `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">systeem_u:systeem_r:container_t:s0:c899,c900</span>
