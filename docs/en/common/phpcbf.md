---
layout: page
title: common/phpcbf (English)
description: "Fix violations detected by phpcs."
content_hash: 1c2f2995da443e477b265bf5034d6cbbbc0cd0e5
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# phpcbf

Fix violations detected by phpcs.
More information: <https://github.com/squizlabs/PHP_CodeSniffer>.

- Fix issues in the specified directory (defaults to the PEAR standard):

`phpcbf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Display a list of installed coding standards:

`phpcbf -i`

- Specify a coding standard to validate against:

`phpcbf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>` --standard `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">standard</span>

- Specify comma-separated file extensions to include when sniffing:

`phpcbf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>` --extensions `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file_extension(s)</span>

- A comma-separated list of files to load before processing:

`phpcbf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>` --bootstrap `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file(s)</span>

- Don't recurse into subdirectories:

`phpcbf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>` -l`
