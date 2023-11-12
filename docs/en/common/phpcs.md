---
layout: page
title: common/phpcs (English)
description: "Tokenize PHP, JavaScript and CSS files to detect violations of a defined set of coding standards."
content_hash: 39cf03509edd65aee15c288b704b1532c7019700
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# phpcs

Tokenize PHP, JavaScript and CSS files to detect violations of a defined set of coding standards.
More information: <https://github.com/squizlabs/PHP_CodeSniffer>.

- Sniff the specified directory for issues (defaults to the PEAR standard):

`phpcs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Display a list of installed coding standards:

`phpcs -i`

- Specify a coding standard to validate against:

`phpcs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>` --standard `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">standard</span>

- Specify comma-separated file extensions to include when sniffing:

`phpcs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>` --extensions `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file_extension(s)</span>

- Specify the format of the output report (e.g. `full`, `xml`, `json`, `summary`):

`phpcs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>` --report `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">format</span>

- Set config variables to be used during the process:

`phpcs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>` --config-set `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">key</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">value</span>

- A comma-separated list of files to load before processing:

`phpcs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>` --bootstrap `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file(s)</span>

- Don't recurse into subdirectories:

`phpcs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>` -l`
