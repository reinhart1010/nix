---
layout: page
title: common/github-label-sync (English)
description: "A command-line interface for synchronising GitHub labels."
content_hash: 3f7719be4b20d902c8d78eeea1a62a4526fa4813
related_topics:
  - title: Türkçe version
    url: /tr/common/github-label-sync.html
    icon: bi bi-globe
---
# github-label-sync

A command-line interface for synchronising GitHub labels.
More information: <https://github.com/Financial-Times/github-label-sync>.

- Synchronise labels using a local `labels.json` file:

`github-label-sync --access-token `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">token</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">repository_name</span>

- Synchronise labels using a specific labels JSON file:

`github-label-sync --access-token `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">token</span>` --labels `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url|path/to/json_file</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">repository_name</span>

- Perform a dry run instead of actually synchronising labels:

`github-label-sync --access-token `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">token</span>` --dry-run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">repository_name</span>

- Keep labels that aren't in `labels.json`:

`github-label-sync --access-token `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">token</span>` --allow-added-labels `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">repository_name</span>

- Synchronise using the `GITHUB_ACCESS_TOKEN` environment variable:

`github-label-sync `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">repository_name</span>
