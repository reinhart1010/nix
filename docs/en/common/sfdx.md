---
layout: page
title: common/sfdx (English)
description: "Command-line tool for development and build automation with a Salesforce organization."
content_hash: 0c3d1a78146b0b8b40f91696ae7a9b4c8a4eb34b
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># sfdx

Command-line tool for development and build automation with a Salesforce organization.
More information: <https://developer.salesforce.com/tools/sfdxcli>.

- Authorize a Salesforce Organization:

`sfdx force:auth:web:login --setalias `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">organization</span>` --instanceurl `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">organization_url</span>

- List all authorized organizations:

`sfdx force:org:list`

- Open a specific organization in the default web browser:

`sfdx force:org:open --targetusername `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">organization</span>

- Display information about a specific organization:

`sfdx force:org:display --targetusername `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">organization</span>

- Push source metadata to an Organization:

`sfdx force:source:push --targetusername `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">organization</span>

- Pull source metadata from an Organization:

`sfdx force:source:pull --targetusername `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">organization</span>

- Generate a password for the organization's logged-in user:

`sfdx force:user:password:generate --targetusername `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">organization</span>

- Assign a permission set for the organization's logged-in user:

`sfdx force:user:permset:assign --permsetname `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">permission_set_name</span>` --targetusername `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">organization</span>
