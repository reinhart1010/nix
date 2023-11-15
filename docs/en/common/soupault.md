---
layout: page
title: common/soupault (English)
description: "A static website generator based on HTML element tree rewriting."
content_hash: 6e01ceb76fb43b3e194d6b0387cb1cbbdbf2e096
last_modified_at: 2023-11-15
tldri18n_status: 2
---
# soupault

A static website generator based on HTML element tree rewriting.
It can also be used as an HTML post-processor or metadata extractor.
More information: <https://soupault.app>.

- Initialize a minimal website project in the current working directory:

`soupault --init`

- Build a website:

`soupault`

- Override default config file and directory locations:

`soupault --config `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">config_path</span>` --site-dir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">input_dir</span>` --build-dir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">output_dir</span>

- Extract metadata into a JSON file without generating pages:

`soupault --index-only --dump-index-json `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.json</span>

- Show the effective config (values from `soupault.toml` plus defaults):

`soupault --show-effective-config`
