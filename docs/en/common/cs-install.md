---
layout: page
title: common/cs-install (English)
description: "Install an application in the installation directory onfigured when installing `cs` (to enable the binary to be loaded add to your `.bash_profile` the `$ eval \"$(cs install --env)\"` command)."
content_hash: 83415ab721d53b714f3f2e35ab72570b2b50d6b7
last_modified_at: 2023-06-14
---
# cs install

Install an application in the installation directory onfigured when installing `cs` (to enable the binary to be loaded add to your `.bash_profile` the `$ eval "$(cs install --env)"` command).
More information: <https://get-coursier.io/docs/cli-install>.

- Install a specific application:

`cs install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">application_name</span>

- Install a specific version of an application:

`cs install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">application_name</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">application_version</span>

- Search an application by a specific name:

`cs search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">application_partial_name</span>

- Update a specific application if available:

`cs update `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">application_name</span>

- Update all the installed applications:

`cs update`

- Uninstall a specific application:

`cs uninstall `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">application_name</span>

- List all installed applications:

`cs list`

- Pass specific java options to an installed application:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">application_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-Jjava_option_name1=value1 -Jjava_option_name2=value2 ...</span>
