---
layout: page
title: common/turbo (English)
description: "High-performance build system for JavaScript and TypeScript codebases."
content_hash: b24a01ca5147b1595d13369b0248f263f6d472b1
last_modified_at: 2023-11-12
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

`turbo run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">task_name</span>` --graph=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>`.`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">html|jpg|json|pdf|png|svg</span>
