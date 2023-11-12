---
layout: page
title: common/ansible-galaxy (italiano)
description: "Crea e gestisci ruoli di Ansible."
content_hash: 32ba735aae3dc4a95648f67d9ea63c58f6393972
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/ansible-galaxy.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/ansible-galaxy.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/ansible-galaxy.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/ansible-galaxy.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/ansible-galaxy.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ansible-galaxy

Crea e gestisci ruoli di Ansible.
Maggiori informazioni: <https://docs.ansible.com/ansible/latest/cli/ansible-galaxy.html>.

- Installa un ruolo:

`ansible-galaxy install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">utente.ruolo</span>

- Rimuovi un ruolo:

`ansible-galaxy remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">utente.ruolo</span>

- Elenca i ruoli installati:

`ansible-galaxy list`

- Cerca un determinato ruolo:

`ansible-galaxy search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_ruolo</span>

- Crea un nuovo ruolo:

`ansible-galaxy init `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_nuovo_ruolo</span>

- Acquisisci informazioni su un ruolo di un utente:

`ansible-galaxy role info `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_utente</span>`.`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_ruolo</span>

- Acquisisci informazioni su una collection:

`ansible-galaxy collection info `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_utente</span>`.`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_raccolta</span>
