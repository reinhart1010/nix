---
layout: page
title: linux/bluebuild (English)
description: "Build Containerfiles and custom images based on your `recipe.yml`."
content_hash: 2ef5e97a1d3bec06a3313290accb7e85592ed571
last_modified_at: 2025-03-02
related_topics:
  - title: español version
    url: /es/linux/bluebuild.html
    icon: bi bi-globe
tldri18n_status: 2
---
# bluebuild

Build Containerfiles and custom images based on your `recipe.yml`.
More information: <https://github.com/blue-build/cli>.

- Build a recipe:

`bluebuild build `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/recipe.yml</span>

- Validate a recipe:

`bluebuild validate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/recipe.yml</span>

- Generate a Containerfile:

`bluebuild generate --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Containerfile</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/recipe.yml</span>

- Generate an ISO from a recipe:

`bluebuild generate-iso --output-dir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output_directory</span>` --iso-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">iso_name.iso</span>` recipe `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/recipe.yml</span>

- Display help:

`bluebuild --help`
