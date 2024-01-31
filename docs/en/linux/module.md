---
layout: page
title: linux/module (English)
description: "Modify a users' environment using the module command."
content_hash: 9f110d08945e4a70f2585ec8eed0e3f029829523
last_modified_at: 2024-01-31
tldri18n_status: 2
---
# module

Modify a users' environment using the module command.
More information: <https://lmod.readthedocs.io/en/latest/010_user.html>.

- Display available modules:

`module avail`

- Search for a module by name:

`module avail `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">module_name</span>

- Load a module:

`module load `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">module_name</span>

- Display loaded modules:

`module list`

- Unload a specific loaded module:

`module unload `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">module_name</span>

- Unload all loaded modules:

`module purge`

- Specify user-created modules:

`module use `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/module_file1 path/to/module_file2 ...</span>
