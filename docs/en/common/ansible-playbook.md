---
layout: page
title: common/ansible-playbook (English)
description: "Execute tasks defined in playbook on remote machines over SSH."
content_hash: f97216f8314a0444b537713e3583a13f4b903323
related_topics:
  - title: Deutsch version
    url: /de/common/ansible-playbook.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/ansible-playbook.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/ansible-playbook.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/ansible-playbook.html
    icon: bi bi-globe
---
# ansible-playbook

Execute tasks defined in playbook on remote machines over SSH.
More information: <https://docs.ansible.com/ansible/latest/cli/ansible-playbook.html>.

- Run tasks in playbook:

`ansible-playbook `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">playbook</span>

- Run tasks in playbook with custom host inventory:

`ansible-playbook `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">playbook</span>` -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">inventory_file</span>

- Run tasks in playbook with extra variables defined via the command-line:

`ansible-playbook `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">playbook</span>` -e "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">variable1</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">value1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">variable2</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">value2</span>`"`

- Run tasks in playbook with extra variables defined in a JSON file:

`ansible-playbook `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">playbook</span>` -e "@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">variables.json</span>`"`

- Run tasks in playbook for the given tags:

`ansible-playbook `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">playbook</span>` --tags `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tag1,tag2</span>

- Run tasks in a playbook starting at a specific task:

`ansible-playbook `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">playbook</span>` --start-at `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">task_name</span>
