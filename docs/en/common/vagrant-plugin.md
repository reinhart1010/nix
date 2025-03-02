---
layout: page
title: common/vagrant-plugin (English)
description: "Manage Vagrant plugins."
content_hash: 6d9c23bdc62ace1350707d88227a8fdb01d7ad78
last_modified_at: 2025-03-02
related_topics:
  - title: español version
    url: /es/common/vagrant-plugin.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/vagrant-plugin.html
    icon: bi bi-globe
tldri18n_status: 2
---
# vagrant plugin

Manage Vagrant plugins.
See also: `vagrant`.
More information: <https://developer.hashicorp.com/vagrant/docs/cli/plugin>.

- List all the plugins currently installed:

`vagrant plugin list`

- Install a plugin from remote repositories, usually RubyGems:

`vagrant plugin install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vagrant_vbguest</span>

- Install a plugin from a local file source:

`vagrant plugin install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/my_plugin.gem</span>

- Update all installed plugins to their latest version:

`vagrant plugin update`

- Update a plugin to the latest version:

`vagrant plugin update `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vagrant_vbguest</span>

- Uninstall a specific plugin:

`vagrant plugin uninstall `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vagrant_vbguest</span>
