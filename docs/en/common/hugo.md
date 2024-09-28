---
layout: page
title: common/hugo (English)
description: "Template-based static site generator. Uses modules, components, and themes."
content_hash: 0b5cf67406477da01f73d974e61beb74a457cb1a
last_modified_at: 2024-09-28
related_topics:
  - title: Indonesia version
    url: /id/common/hugo.html
    icon: bi bi-globe
tldri18n_status: 2
---
# hugo

Template-based static site generator. Uses modules, components, and themes.
Some subcommands such as `server` have their own usage documentation.
More information: <https://gohugo.io>.

- Create a new Hugo site:

`hugo new site `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/site</span>

- Create a new Hugo theme (themes may also be downloaded from <https://themes.gohugo.io/>):

`hugo new theme `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">theme_name</span>

- Create a new page:

`hugo new `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">section_name</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">page_name</span>

- Build a site to the `./public/` directory:

`hugo`

- Build a site including pages that are marked as a "draft":

`hugo --buildDrafts`

- Build a site on your local IP:

`hugo server --bind `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">local-ip</span>` --baseURL `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://local-ip</span>

- Build a site to a given directory:

`hugo --destination `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/destination</span>

- Build a site, start up a webserver to serve it, and automatically reload when pages are edited:

`hugo server`
