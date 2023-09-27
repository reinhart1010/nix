---
layout: page
title: common/rustic (English)
description: "Create fast, encrypted, deduplicated backups powered by Rust."
content_hash: a01c9d2c096ab78f7ae3914d069747de79f11913
last_modified_at: 2023-09-27
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># rustic

Create fast, encrypted, deduplicated backups powered by Rust.
More information: <https://github.com/rustic-rs/rustic>.

- Initialize a new repository:

`rustic init --repository `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/srv/rustic-repo</span>

- Create a new backup of a file/directory to a repository:

`rustic backup --repository `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/srv/rustic-repo</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file_or_directory</span>
