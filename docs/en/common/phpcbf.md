---
layout: page
title: common/phpcbf (English)
description: "Fix violations detected by phpcs."
content_hash: 065ae7610b0e06f6c8f93f5d6c50324af2fae61f
last_modified_at: 2024-01-31
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

`phpcbf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>` --extensions `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file_extension1,file_extension2,...</span>

- A comma-separated list of files to load before processing:

`phpcbf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>` --bootstrap `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1,path/to/file2,...)</span>

- Don't recurse into subdirectories:

`phpcbf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>` -l`
