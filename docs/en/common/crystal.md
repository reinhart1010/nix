---
layout: page
title: common/crystal (English)
description: "Manage Crystal source code."
content_hash: 8f8c7bc81ed6fdfef3586b6ffd9e986a28210e82
last_modified_at: 2024-02-15
related_topics:
  - title: français version
    url: /fr/common/crystal.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/crystal.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/crystal.html
    icon: bi bi-globe
tldri18n_status: 2
---
# crystal

Manage Crystal source code.
More information: <https://crystal-lang.org/reference/using_the_compiler>.

- Run a Crystal file:

`crystal `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.cr</span>

- Compile a file and all dependencies to a single executable:

`crystal build `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.cr</span>

- Read Crystal source code from the command line or `stdin`, and execute it:

`crystal eval '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">code</span>`'`

- Generate API documentation from inline docstrings in Crystal files:

`crystal docs`

- Compile and run a Crystal specification suite:

`crystal spec`

- Start a local interactive server for testing the language:

`crystal play`

- Create a project directory for a Crystal application:

`crystal init app `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">application_name</span>

- Display all help options:

`crystal help`
