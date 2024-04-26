---
layout: page
title: common/black (English)
description: "Format Python code automatically."
content_hash: 29ad910d8e338717704830cf6584d9e77ed9c9af
last_modified_at: 2024-04-26
related_topics:
  - title: italiano version
    url: /it/common/black.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/black.html
    icon: bi bi-globe
tldri18n_status: 2
---
# black

Format Python code automatically.
More information: <https://black.readthedocs.io/en/stable/usage_and_configuration/the_basics.html>.

- Auto-format a file or entire directory:

`black `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file_or_directory</span>

- Format the [c]ode passed in as a string:

`black -c "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">code</span>`"`

- Show whether a file or a directory would have changes made to them if they were to be formatted:

`black --check `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file_or_directory</span>

- Show changes that would be made to a file or a directory without performing them (dry-run):

`black --diff `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file_or_directory</span>

- Auto-format a file or directory, emitting exclusively error messages to `stderr`:

`black --quiet `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file_or_directory</span>

- Auto-format a file or directory without replacing single quotes with double quotes (adoption helper, avoid using this for new projects):

`black --skip-string-normalization `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file_or_directory</span>
