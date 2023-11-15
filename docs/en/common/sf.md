---
layout: page
title: common/sf (English)
description: "A powerful command line interface that simplifies development and build automation when working with your Salesforce org."
content_hash: 2908a24d314df7e41c4324586e34838681ba927e
last_modified_at: 2023-11-15
tldri18n_status: 2
---
# sf

A powerful command line interface that simplifies development and build automation when working with your Salesforce org.
More information: <https://developer.salesforce.com/tools/salesforcecli>.

- Authorize a Salesforce Organization:

`sf force:auth:web:login --setalias `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">organization</span>` --instanceurl `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">organization_url</span>

- List all authorized organizations:

`sf force:org:list`

- Open a specific organization in the default web browser:

`sf force:org:open --targetusername `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">organization</span>

- Display information about a specific organization:

`sf force:org:display --targetusername `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">organization</span>

- Push source metadata to an Organization:

`sf force:source:push --targetusername `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">organization</span>

- Pull source metadata from an Organization:

`sf force:source:pull --targetusername `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">organization</span>

- Generate a password for the organization's logged-in user:

`sf force:user:password:generate --targetusername `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">organization</span>

- Assign a permission set for the organization's logged-in user:

`sf force:user:permset:assign --permsetname `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">permission_set_name</span>` --targetusername `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">organization</span>
