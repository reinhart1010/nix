---
layout: page
title: common/ruby (English)
description: "Ruby programming language interpreter."
content_hash: 400bd081a01ce1931bb89a08c20b87d69e82cc3e
last_modified_at: 2024-01-30
related_topics:
  - title: français version
    url: /fr/common/ruby.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/ruby.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/ruby.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ruby

Ruby programming language interpreter.
See also: `gem`, `bundler`, `rake`, `irb`.
More information: <https://www.ruby-lang.org>.

- Execute a Ruby script:

`ruby `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">script.rb</span>

- Execute a single Ruby command in the command-line:

`ruby -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>

- Check for syntax errors on a given Ruby script:

`ruby -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">script.rb</span>

- Start the built-in HTTP server on port 8080 in the current directory:

`ruby -run -e httpd`

- Locally execute a Ruby binary without installing the required library it depends on:

`ruby -I `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/library_folder</span>` -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">library_require_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/bin_folder/bin_name</span>

- Display Ruby version:

`ruby -v`
