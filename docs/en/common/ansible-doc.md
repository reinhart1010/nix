---
layout: page
title: common/ansible-doc (English)
description: "Display information on modules installed in Ansible libraries."
content_hash: fb5ffc56221d9a6f237e4675f1a910c8dfc6b538
---
# ansible-doc

Display information on modules installed in Ansible libraries.
Display a terse listing of plugins and their short descriptions.
More information: <https://docs.ansible.com/ansible/latest/cli/ansible-doc.html>.

- List available action plugins (modules):

`ansible-doc --list`

- List available plugins of a specific type:

`ansible-doc --type `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">plugin_type</span>` --list`

- Show information about a specific action plugin (module):

`ansible-doc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">plugin_name</span>

- Show information about a plugin with a specific type:

`ansible-doc --type `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">plugin_type</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">plugin_name</span>

- Show the playbook snippet for action plugin (modules):

`ansible-doc --snippet `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">plugin_name</span>

- Show information about an action plugin (module) as JSON:

`ansible-doc --json `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">plugin_name</span>
