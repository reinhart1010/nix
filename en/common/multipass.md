---
layout: page
title: common/multipass (English)
description: "CLI to manage Ubuntu virtual machines using native hypervisors."
content_hash: b262057286bc066dec293c4cbe64bc41dcf0f3ec
---
# multipass

CLI to manage Ubuntu virtual machines using native hypervisors.
More information: <https://multipass.run/>.

- List the aliases that can be used to launch an instance:

`multipass find`

- Launch a new instance, set its name and use a cloud-init configuration file:

`multipass launch -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">instance_name</span>` --cloud-init `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">configuration_file</span>

- List all the created instances and some of their properties:

`multipass list`

- Start a specific instance by name:

`multipass start `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">instance_name</span>

- Show the properties of an instance:

`multipass info `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">instance_name</span>

- Open a shell prompt on a specific instance by name:

`multipass shell `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">instance_name</span>

- Delete an instance by name:

`multipass delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">instance_name</span>

- Mount a directory into a specific instance:

`multipass mount `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/local/directory</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">instance_name</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/target/directory</span>
