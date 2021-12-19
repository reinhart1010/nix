---
layout: page
title: common/ansible (italiano)
description: "Gestisce gruppi di computer da remoto via SSH."
content_hash: 6ebcfe8d5cbe2953e1dd21275f936cbdd1eb6841
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
  - title: 한국어 version
    url: /ko/common/ansible.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/ansible.html
    icon: bi bi-globe
---
# ansible

Gestisce gruppi di computer da remoto via SSH.
Usa il file `/etc/ansible/hosts` per aggiungere nuovi gruppi/host.
Alcuni comandi aggiuntivi, come `ansible galaxy`, hanno la propria documentazione.
Maggiori informazioni: <https://www.ansible.com/>.

- Elenca gli host appartenenti ad un gruppo:

`ansible `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gruppo</span>` --list-hosts`

- Invia un ping ad un gruppo di host invocando il modulo "ping":

`ansible `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gruppo</span>` -m ping`

- Mostra informazioni su un gruppo di host invocando il modulo "setup":

`ansible `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gruppo</span>` -m setup`

- Esegui un comando su un gruppo di host invocando il modulo "command" con degli argomenti:

`ansible `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gruppo</span>` -m command -a '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando_da_eseguire</span>`'`

- Esegui un comando con privilegi di amministratore:

`ansible `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gruppo</span>` --become --ask-become-pass -m command -a '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando</span>`'`

- Esegui un comando usando un file di inventory personalizzato:

`ansible `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gruppo</span>` -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file_inventory</span>` -m command -a '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando</span>`'`

- Elenca i gruppi in un inventory:

`ansible localhost -m debug -a '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">var=groups.keys()</span>`'`
