---
layout: page
title: windows/octo (English)
description: "Command-line tools for Octopus Deploy."
content_hash: 0a30f6478c0439f3700286bb5bdc0043d0d7ac85
last_modified_at: 2023-08-26
---
# octo

Command-line tools for Octopus Deploy.
More information: <https://octopus.com/docs/octopus-rest-api/octo.exe-command-line>.

- Create a package:

`octo pack --id=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- Push a package to a repository on the Octopus server:

`octo push --package=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- Create a release:

`octo create-release --project=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">project_name</span>` --packageversion=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">version</span>

- Deploy a release:

`octo deploy-release --project=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">project_name</span>` --packageversion=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">version</span>` --deployto=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">environment_name</span>` --tenant=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">deployment_target</span>
