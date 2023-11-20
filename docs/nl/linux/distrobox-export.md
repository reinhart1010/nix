---
layout: page
title: linux/distrobox-export (Nederlands)
description: "Exporteer app/service/binary van container naar host-besturingssysteem."
content_hash: 5172062a9e84631010e8342479c4a3dea5687514
last_modified_at: 2023-11-20
related_topics:
  - title: English version
    url: /en/linux/distrobox-export.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/distrobox-export.html
    icon: bi bi-globe
tldri18n_status: 2
---
# distrobox-export

Exporteer app/service/binary van container naar host-besturingssysteem.
Subcommando van `distrobox`. Bekijk ook: `tldr distrobox`.
Meer informatie: <https://distrobox.it/usage/distrobox-export>.

- Exporteer een app van de container naar de host (het desktop pictogram verschijnt in de applicatielijst van uw hostsysteem):

`distrobox-export --app `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pakket</span>` --extra-flags "--foreground"`

- Exporteer een binary van de container naar de host:

`distrobox-export --bin `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/binary</span>` --export-path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/binary_on_host</span>

- Exporteer een binary van de container naar de host (bijv.`$HOME/.local/bin`) :

`distrobox-export --bin `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/binary</span>` --export-path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/export</span>

- Exporteer een service van de container naar de host (`--sudo` zal de service uitvoeren als root in de container):

`distrobox-export --service `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pakket</span>` --extra-flags "--allow-newer-config" --sudo`

- Verwijder een geëxporteerde applicatie:

`distrobox-export --app `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pakket</span>` --delete`
