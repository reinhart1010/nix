---
layout: page
title: common/surge (English)
description: "Simple web publishing."
content_hash: 3f935656715b3a2b5c1edb8958683d8ff95a7187
last_modified_at: 2023-07-16
---
# surge

Simple web publishing.
More information: <https://surge.sh>.

- Upload a new site to surge.sh:

`surge `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/my_project</span>

- Deploy site to custom domain (note that the DNS records must point to the surge.sh subdomain):

`surge `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/my_project</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">my_custom_domain.com</span>

- List your surge projects:

`surge list`

- Remove a project:

`surge teardown `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">my_custom_domain.com</span>
