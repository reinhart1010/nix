---
layout: page
title: common/zola (English)
description: "A static site generator in a single binary with everything built-in."
content_hash: 0a4b2be94d7ae276b461709be5f5b5e6832fee88
last_modified_at: 2023-11-12
related_topics:
  - title: français version
    url: /fr/common/zola.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/zola.html
    icon: bi bi-globe
tldri18n_status: 2
---
# zola

A static site generator in a single binary with everything built-in.
More information: <https://www.getzola.org/documentation/getting-started/cli-usage/>.

- Create the directory structure used by Zola at the given directory:

`zola init `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">my_site</span>

- Build the whole site in the `public` directory after deleting it:

`zola build`

- Build the whole site into a different directory:

`zola build --output-dir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output_directory/</span>

- Build and serve the site using a local server (default is `127.0.0.1:1111`):

`zola serve`

- Build all pages just like the build command would, but without writing any of the results to disk:

`zola check`
