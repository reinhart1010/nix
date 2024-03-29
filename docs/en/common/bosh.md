---
layout: page
title: common/bosh (English)
description: "Deploy and manage the BOSH director."
content_hash: 0221fc2646343465657720021aa672492befff0b
last_modified_at: 2024-02-19
related_topics:
  - title: italiano version
    url: /it/common/bosh.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/bosh.html
    icon: bi bi-globe
tldri18n_status: 2
---
# bosh

Deploy and manage the BOSH director.
More information: <https://bosh.io/docs/cli-v2/>.

- Create local alias for director in a specific [e]nvironment:

`bosh alias-env `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">environment_name</span>` -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip_address|URL</span>` --ca-cert `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ca_certificate</span>

- List environments:

`bosh environments`

- Log in to the director:

`bosh login -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">environment</span>

- List deployments:

`bosh -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">environment</span>` deployments`

- List environment virtual machines in a [d]eployment:

`bosh -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">environment</span>` vms -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">deployment</span>

- SSH into virtual machine:

`bosh -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">environment</span>` ssh `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">virtual_machine</span>` -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">deployment</span>

- Upload stemcell:

`bosh -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">environment</span>` upload-stemcell `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">stemcell_file|url</span>

- Show current cloud config:

`bosh -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">environment</span>` cloud-config`
