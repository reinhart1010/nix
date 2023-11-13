---
layout: page
title: common/ansible (Nederlands)
description: "Beheer een groep van computers op afstand over SSH. (Gebruik het `/etc/ansible/hosts` bestand om nieuwe groepen/hosts toe te voegen)."
content_hash: 45740abe42f4f00fd65dd4312502f2ae0f7d9a89
last_modified_at: 2023-11-13
related_topics:
  - title: Deutsch version
    url: /de/common/ansible.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/ansible.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/ansible.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/ansible.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/ansible.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/ansible.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/ansible.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/ansible.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># ansible

Beheer een groep van computers op afstand over SSH. (Gebruik het `/etc/ansible/hosts` bestand om nieuwe groepen/hosts toe te voegen).
Sommige subcommando's zoals `ansible galaxy` hebben hun eigen documentatie.
Meer informatie: <https://www.ansible.com/>.

- Toon de hosts die tot een groep behoren:

`ansible `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">groep</span>` --list-hosts`

- Ping een groep met hosts, met gebruik van de ping module:

`ansible `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">groep</span>` -m ping`

- Toon feiten van een groep met hosts, met gebruik van de installatie module:

`ansible `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">groep</span>` -m setup`

- Voer een commando op een groep met hosts uit. met gebruik van de commando module met argumenten:

`ansible `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">groep</span>` -m command -a '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mijn_commando</span>`'`

- Voer een commando uit met administratieve rechten:

`ansible `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">groep</span>` --become --ask-become-pass -m command -a '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mijn_commando</span>`'`

- Voer een commando uit met een aangepast inventaris bestand:

`ansible `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">groep</span>` -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">inventaris_bestand</span>` -m command -a '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mijn_command</span>`'`

- Toon de groepen in een inventaris:

`ansible localhost -m debug -a '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">var=groups.keys()</span>`'`
