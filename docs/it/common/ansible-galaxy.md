---
layout: page
title: common/ansible-galaxy (italiano)
description: "Esegui varie operazioni inerenti ai Ruoli e alle Collezioni in Ansible."
content_hash: 07a5e08c8a8ee64553fe9662703c3e13224f424e
last_modified_at: 2024-12-22
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
  - title: Indonesia version
    url: /id/common/ansible-galaxy.html
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

Esegui varie operazioni inerenti ai Ruoli e alle Collezioni in Ansible.
Maggiori informazioni: <https://docs.ansible.com/ansible/latest/cli/ansible-galaxy.html>.

- Lista i ruoli o le collezioni installate:

`ansible-galaxy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruolo|collezione</span>` list`

- Cerca un ruolo con vari livelli di verbosità (`-v` deve essere specificato alla fine):

`ansible-galaxy role search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">keyword</span>` -v`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vvvvv</span>

- Installa o rimuovi ruoli:

`ansible-galaxy role `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">install|remove</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_ruolo1 nome_ruolo2 ...</span>

- Crea un nuovo ruolo:

`ansible-galaxy role init `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_ruolo</span>

- Ottieni informazioni inerenti a un ruolo:

`ansible-galaxy role info `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_ruolo</span>

- Installa o rimuovi collezioni:

`ansible-galaxy collection `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">install|remove</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_collezione1 nome_collezione2 ...</span>

- Mostra aiuto su ruoli o collezioni:

`ansible-galaxy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruolo|collezione</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-h|--help</span>
