---
layout: page
title: common/rake (English)
description: "A Make-like program for Ruby."
content_hash: 16e4f8542a0184f209c1d89edc090eb31e3d8399
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# rake

A Make-like program for Ruby.
Tasks for `rake` are specified in a Rakefile.
More information: <https://ruby.github.io/rake>.

- Run the `default` Rakefile task:

`rake`

- Run a specific task:

`rake `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">task</span>

- Execute `n` jobs at a time in parallel (number of CPU cores + 4 by default):

`rake --jobs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">n</span>

- Use a specific Rakefile:

`rake --rakefile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/Rakefile</span>

- Execute `rake` from another directory:

`rake --directory `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>
