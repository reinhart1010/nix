---
layout: page
title: common/ansible-doc (English)
description: "Display information on modules installed in Ansible libraries."
content_hash: 40846412d891a5419a60e5e9822b045f364caa44
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/ansible-doc.html
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

Display information on modules installed in Ansible libraries.
Display a terse listing of plugins and their short descriptions.
More information: <https://docs.ansible.com/ansible/latest/cli/ansible-doc.html>.

- List available action plugins (modules):

`ansible-doc --list`

- List available plugins of a specific type:

`ansible-doc --type `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">become|cache|callback|cliconf|connection|...</span>` --list`

- Show information about a specific action plugin (module):

`ansible-doc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">plugin_name</span>

- Show information about a plugin with a specific type:

`ansible-doc --type `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">become|cache|callback|cliconf|connection|...</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">plugin_name</span>

- Show the playbook snippet for action plugin (modules):

`ansible-doc --snippet `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">plugin_name</span>

- Show information about an action plugin (module) as JSON:

`ansible-doc --json `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">plugin_name</span>
