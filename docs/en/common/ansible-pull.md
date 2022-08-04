---
layout: page
title: common/ansible-pull (English)
description: "Pull ansible playbooks from a VCS repo and executes them for the local host."
content_hash: 366afa2faaff48332c9139fe75e45ca9618be59c
---
# ansible-pull

Pull ansible playbooks from a VCS repo and executes them for the local host.
More information: <https://docs.ansible.com/ansible/latest/cli/ansible-pull.html>.

- Pull a playbook from a VCS and execute a default local.yml playbook:

`ansible-pull -U `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">repository_url</span>

- Pull a playbook from a VCS and execute a specific playbook:

`ansible-pull -U `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">repository_url</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">playbook</span>

- Pull a playbook from a VCS at a specific branch and execute a specific playbook:

`ansible-pull -U `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">repository_url</span>` -C `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">branch</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">playbook</span>

- Pull a playbook from a VCS, specify hosts file and execute a specific playbook:

`ansible-pull -U `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">repository_url</span>` -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hosts_file</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">playbook</span>
