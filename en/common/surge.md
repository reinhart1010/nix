---
layout: page
title: common/surge (English)
description: "Simple command-line web publishing."
content_hash: cc0d64ad1818cca5dde7093658d8ab9bac666db0
---
# surge

Simple command-line web publishing.
More information: <https://surge.sh>.

- Upload a new site to surge.sh:

`surge `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/my_project</span>

- Deploy site to custom domain (note that the DNS records must point to the surge.sh subdomain):

`surge `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/my_project</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">my_custom_domain.com</span>

- List your surge projects:

`surge list`

- Remove a project:

`surge teardown `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">my_custom_domain.com</span>
