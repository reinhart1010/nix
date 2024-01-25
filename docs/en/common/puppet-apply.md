---
layout: page
title: common/puppet-apply (English)
description: "Apply Puppet manifests locally."
content_hash: ff36bfe3d35eb59ef7d296cd1d2d1180a52fbc33
last_modified_at: 2024-01-25
related_topics:
  - title: Deutsch version
    url: /de/common/puppet-apply.html
    icon: bi bi-globe
tldri18n_status: 2
---
# puppet apply

Apply Puppet manifests locally.
More information: <https://puppet.com/docs/puppet/7/man/apply.html>.

- Apply a manifest:

`puppet apply `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/manifest</span>

- Execute puppet code:

`puppet apply --execute `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">code</span>

- Use a specific module and hiera configuration file:

`puppet apply --modulepath `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>` --hiera_config `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/manifest</span>
