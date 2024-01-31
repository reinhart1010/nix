---
layout: page
title: common/phpstan (English)
description: "A PHP static analysis tool to discover bugs in code."
content_hash: 348c5a29f12bb6e93c704c81f4683ea593ed08e4
last_modified_at: 2024-01-31
tldri18n_status: 2
---
# phpstan

A PHP static analysis tool to discover bugs in code.
More information: <https://github.com/phpstan/phpstan>.

- Analyze one or more directories:

`phpstan analyse `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory1 path/to/directory2 ...</span>

- Analyze a directory using a configuration file:

`phpstan analyse `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>` --configuration `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/config</span>

- Analyze using a specific rule level (0-7, higher is stricter):

`phpstan analyse `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>` --level `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">level</span>

- Specify an autoload file to load before analyzing:

`phpstan analyse `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>` --autoload-file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/autoload_file</span>

- Specify a memory limit during analysis:

`phpstan analyse `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>` --memory-limit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">memory_limit</span>

- Display available options for analysis:

`phpstan analyse --help`
