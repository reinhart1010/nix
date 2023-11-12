---
layout: page
title: common/ansible-doc (Deutsch)
description: "Anzeigen von Informationen über die in den Ansible-Bibliotheken installierten Module."
content_hash: 11700a21fd69f4462ddfe5f296bdeda27027ae84
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/ansible-doc.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/ansible-doc.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/ansible-doc.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ansible-doc

Anzeigen von Informationen über die in den Ansible-Bibliotheken installierten Module.
Anzeigen einer knappen Auflistung von Plugins und deren Kurzbeschreibungen.
Weitere Informationen: <https://docs.ansible.com/ansible/latest/cli/ansible-doc.html>.

- Auflisten der verfügbaren Aktions-Plugin (Module):

`ansible-doc --list`

- Auflisten der verfügbare Plugins eines bestimmten Typs:

`ansible-doc --type `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">plugin_typ</span>` --list`

- Anzeigen von Informationen über ein bestimmtes Aktions-Plugin (Module):

`ansible-doc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">plugin_name</span>

- Anzeigen von Informationen über ein Plugin mit einem betimmten Typ:

`ansible-doc --type `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">plugin_typ</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">plugin_name</span>

- Anzeigen des Playbookausschnittes für ein Actions-Plugin (Module):

`ansible-doc --snippet `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">plugin_name</span>

- Anzeigen von Informationen über ein Aktions-Plugin (Module) als JSON:

`ansible-doc --json `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">plugin_name</span>
