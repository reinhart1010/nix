---
layout: page
title: common/ansible-galaxy (Deutsch)
description: "Erstelle und verwalte Ansible Rollen."
content_hash: c6c96669c70463e8f6ec8164e8a7fe0b3a2592c4
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/ansible-galaxy.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/ansible-galaxy.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/ansible-galaxy.html
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

Erstelle und verwalte Ansible Rollen.
Weitere Informationen: <https://docs.ansible.com/ansible/latest/cli/ansible-galaxy.html>.

- Installiere eine Rolle:

`ansible-galaxy install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">benutzername</span>`.`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">rollenname</span>

- Entferne eine Rolle:

`ansible-galaxy remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">benutzername</span>`.`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">rollenname</span>

- Liste installierte Rollen auf:

`ansible-galaxy list`

- Suche nach einer bestimmten Rolle:

`ansible-galaxy search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">rollenname</span>

- Erstelle eine neue Rolle:

`ansible-galaxy init `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">rollenname</span>

- Erhalte Informationen über eine Benutzerrolle:

`ansible-galaxy role info `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">benutzername</span>`.`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">rollenname</span>

- Erhalte Informationen über eine Kollektion:

`ansible-galaxy collection info `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">benutzername</span>`.`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">kollektionsname</span>
