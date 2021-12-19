---
layout: page
title: common/github-label-sync (English)
description: "A command-line interface for synchronising GitHub labels."
content_hash: e42d4d80ee4028838e957b3f96ace7e02024e4a4
---
# github-label-sync

A command-line interface for synchronising GitHub labels.
More information: <https://npmjs.com/package/github-label-sync>.

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
