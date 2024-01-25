---
layout: page
title: common/phan (English)
description: "A static analysis tool for PHP."
content_hash: 3c9790da81f6ee330921365e2e647bfb02bcf280
last_modified_at: 2024-01-25
tldri18n_status: 2
---
# phan

A static analysis tool for PHP.
More information: <https://github.com/phan/phan>.

- Generate a `.phan/config.php` in the current directory:

`phan --init`

- Generate a Phan configuration file using a specific level (1 being strictest to 5 being the least strict):

`phan --init --init-level `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">level</span>

- Analyze the current directory:

`phan`

- Analyze one or more directories:

`phan --directory `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>` --directory `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/another_directory</span>

- Specify a configuration file (defaults to `.phan/config.php`):

`phan --config-file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/config.php</span>

- Specify the output mode:

`phan --output-mode `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">text|verbose|json|csv|codeclimate|checkstyle|pylint|html</span>

- Specify the number of parallel processes:

`phan --processes `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">number_of_processes</span>
