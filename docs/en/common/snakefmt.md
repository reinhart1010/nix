---
layout: page
title: common/snakefmt (English)
description: "Format Snakemake files."
content_hash: d79f86a79f8ea6f2a856270b57ac192a18527821
last_modified_at: 2023-11-12
related_topics:
  - title: português (Brasil) version
    url: /pt_BR/common/snakefmt.html
    icon: bi bi-globe
tldri18n_status: 2
---
# snakefmt

Format Snakemake files.
More information: <https://github.com/snakemake/snakefmt>.

- Format a specific Snakefile:

`snakefmt `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/snakefile</span>

- Format all Snakefiles recursively in a specific directory:

`snakefmt `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Format a file using a specific configuration file:

`snakefmt --config `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/config.toml</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/snakefile</span>

- Format a file using a specific maximum line length:

`snakefmt --line-length `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">100</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/snakefile</span>

- Display the changes that would be performed without performing them (dry-run):

`snakefmt --diff `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/snakefile</span>
