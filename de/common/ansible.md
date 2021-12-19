---
layout: page
title: common/ansible (Deutsch)
description: "Verwalte Computergruppen per Fernzugriff über SSH (Verwende die Datei `/etc/ansible/hosts`, um neue Gruppen/Hosts hinzuzufügen)."
content_hash: ee4d76a7b01a470f7ccc0d50abcd6a89d1ab5916
related_topics:
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
  - title: 中文 version
    url: /zh/common/ansible.html
    icon: bi bi-globe
---
# ansible

Verwalte Computergruppen per Fernzugriff über SSH (Verwende die Datei `/etc/ansible/hosts`, um neue Gruppen/Hosts hinzuzufügen).
Manche Unterbefehle wie `ansible galaxy` sind separat dokumentiert.
Weitere Informationen: <https://www.ansible.com/>.

- Liste Hosts auf, die zu einer Gruppe gehören:

`ansible `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gruppe</span>` --list-hosts`

- Pinge eine Gruppe von Hosts an:

`ansible `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gruppe</span>` -m ping`

- Zeige Informationen über eine Gruppe von Hosts an:

`ansible `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gruppe</span>` -m setup`

- Führe einen Befehl auf einer Gruppe von Hosts aus:

`ansible `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gruppe</span>` -m command -a '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">befehl</span>`'`

- Führe einen Befehl mit administrativen Privilegien aus:

`ansible `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gruppe</span>` --become --ask-become-pass -m command -a '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">befehl</span>`'`

- Führe einen Befehl mit einer benutzerdefinierten Inventardatei aus:

`ansible `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Gruppe</span>` -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">inventardatei</span>` -m command -a '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">befehl</span>`'`

- Liste alle Gruppen eines Inventars auf:

`ansible localhost -m debug -a '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">var=groups.keys()</span>`'`
