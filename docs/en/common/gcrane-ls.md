---
layout: page
title: common/gcrane-ls (English)
description: "List the tags in a repository."
content_hash: 45634575840df302906927c2661579b7a9e5ca71
last_modified_at: 2024-10-04
tldri18n_status: 2
---
# gcrane ls

List the tags in a repository.
More complex form than `crane ls`, which allows for listing tags, manifest and sub-repositories.
More information: <https://github.com/google/go-containerregistry/blob/main/cmd/gcrane/README.md>.

- List the tags:

`gcrane ls `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">repository</span>

- Format response from the registry as JSON:

`gcrane ls `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">repository</span>` --json`

- Whether to recurse through repositories:

`gcrane ls `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">repository</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-r|--recursive</span>

- Display help:

`gcrane ls `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-h|--help</span>
