---
layout: page
title: common/clip-view (English)
description: "Command Line Interface Pages render."
content_hash: ddbe4a3a1b4d26fc4d57669132374f5b613684e9
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# clip-view

Command Line Interface Pages render.
Render for a TlDr-like project with much a more extensive syntax and several render modes.
More information: <https://github.com/command-line-interface-pages/v2-tooling/tree/main/clip-view>.

- Render specific local pages:

`clip-view `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/page1.clip path/to/page2.clip ...</span>

- Render specific remote pages:

`clip-view `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">page_name1 page_name2 ...</span>

- Render pages by a specific render:

`clip-view --render `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tldr|tldr-colorful|docopt|docopt-colorful</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">page_name1 page_name2 ...</span>

- Render pages with a specific color theme:

`clip-view --theme `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/local_theme.yaml|remote_theme_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">page_name1 page_name2 ...</span>

- Clear a page or theme cache:

`clip-view --clear-`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">page|theme</span>`-cache`

- Display help:

`clip-view --help`

- Display version:

`clip-view --version`
