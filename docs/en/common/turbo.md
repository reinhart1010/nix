---
layout: page
title: common/turbo (English)
description: "High-performance build system for JavaScript and TypeScript codebases."
content_hash: 68ecd07475ed176bd1df36f9900ae16c8ee2077a
last_modified_at: 2024-01-31
tldri18n_status: 2
---
# turbo

High-performance build system for JavaScript and TypeScript codebases.
See also: `nx`.
More information: <https://turborepo.org/docs/reference/command-line-reference>.

- Log in using the default web browser with a Vercel account:

`turbo login`

- Link the current directory to a Vercel organization and enable remote caching:

`turbo link`

- Build the current project:

`turbo run build`

- Run a task without concurrency:

`turbo run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">task_name</span>` --concurrency=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1</span>

- Run a task ignoring cached artifacts and forcibly re-execute all tasks:

`turbo run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">task_name</span>` --force`

- Run a task in parallel across packages:

`turbo run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">task_name</span>` --parallel --no-cache`

- Unlink the current directory from your Vercel organization and disable Remote Caching:

`turbo unlink`

- Generate a Dot graph of a specific task execution (the output file format can be controlled with the filename):

`turbo run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">task_name</span>` --graph=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.html|jpg|json|pdf|png|svg</span>
