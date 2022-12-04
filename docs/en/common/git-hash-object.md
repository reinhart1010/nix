---
layout: page
title: common/git-hash-object (English)
description: "Computes the unique hash key of content and optionally creates an object with specified type."
content_hash: 46db392ea13255434465b241d2688a2c1102c8ab
last_modified_at: 2022-12-04
---
# git hash-object

Computes the unique hash key of content and optionally creates an object with specified type.
More information: <https://git-scm.com/docs/git-hash-object>.

- Compute the object ID without storing it:

`git hash-object `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Compute the object ID and store it in the Git database:

`git hash-object -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Compute the object ID specifying the object type:

`git hash-object -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">blob|commit|tag|tree</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Compute the object ID from `stdin`:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>` | git hash-object --stdin`
