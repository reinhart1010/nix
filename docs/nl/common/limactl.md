---
layout: page
title: common/limactl (Nederlands)
description: "Virtual machine manager voor Linux gasten, met meerdere VM templates beschikbaar."
content_hash: 960a2a47bb9cb744029b755d64c19ddefd5f9dd5
last_modified_at: 2023-11-26
related_topics:
  - title: English version
    url: /en/common/limactl.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/limactl.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># limactl

Virtual machine manager voor Linux gasten, met meerdere VM templates beschikbaar.
Kan worden gebruikt om containers op macOS uit te voeren, maar ook voor generieke virtuele machine use cases op macOS en Linux hosts.
Meer informatie: <https://github.com/lima-vm/lima>.

- Toon VMs:

`limactl list`

- Maak een VM met standaard instellingen en voorzie optioneel van een naam en/of template (zie `limactl create --list-templates` voor beschikbare templates):

`limactl create --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vm_name</span>` template://`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">debian|fedora|ubuntu|…</span>

- Start een VM (dit kan enkele afhankelijkheden erin installeren en een paar minuten duren):

`limactl start `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vm_name</span>

- Open een externe shell in een VM:

`limactl shell `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vm_name</span>

- Voer een commando uit in een VM:

`limactl shell `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vm_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commando</span>

- Stop/sluit een VM af:

`limactl stop `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vm_name</span>

- Verwijder een VM:

`limactl remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vm_name</span>
