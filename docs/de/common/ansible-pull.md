---
layout: page
title: common/ansible-pull (Deutsch)
description: "Laden eines Ansible-Playbooks aus einem VCS-Repository und ausführen auf dem lokalen Host."
content_hash: 58c7849c33a706c8495646e5da98f9f44e304e68
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/ansible-pull.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/ansible-pull.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/ansible-pull.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ansible-pull

Laden eines Ansible-Playbooks aus einem VCS-Repository und ausführen auf dem lokalen Host.
Weitere Informationen: <https://docs.ansible.com/ansible/latest/cli/ansible-pull.html>.

- Laden eines Playbooks aus einem VCS und ausführen des standardmässigen local.yml Playbooks:

`ansible-pull -U `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">repository_url</span>

- Laden eines Playbooks aus einem VCS und ausführen eines spezifischen Playbooks:

`ansible-pull -U `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">repository_url</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">playbook</span>

- Laden eines Playbooks aus einem VCS unter angabe eines bestimmten branches und ausführen eines spezifischen Playbooks:

`ansible-pull -U `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">repository_url</span>` -C `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">branch</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">playbook</span>

- Laden eines Playbooks aus einem VCS und ausführen eines spezifischen Playbooks unter angabe einer Hosts-Datei:

`ansible-pull -U `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">repository_url</span>` -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hosts_datei</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">playbook</span>
