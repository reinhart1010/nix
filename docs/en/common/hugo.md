---
layout: page
title: common/hugo (English)
description: "Template-based static site generator. Uses modules, components, and themes."
content_hash: 875e57534625f46e15b3fc4e191fca20c5a97aca
last_modified_at: 2022-12-06
related_topics:
  - title: Indonesia version
    url: /id/common/hugo.html
    icon: bi bi-globe
---
# hugo

Template-based static site generator. Uses modules, components, and themes.
More information: <https://gohugo.io>.

- Create a new Hugo site:

`hugo new site `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/site</span>

- Create a new Hugo theme (themes may also be downloaded from https://themes.gohugo.io/):

`hugo new theme `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">theme_name</span>

- Create a new page:

`hugo new `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">section_name</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Build a site to the `./public/` directory:

`hugo`

- Build a site including pages that are marked as a "draft":

`hugo --buildDrafts`

- Build a site to a given directory:

`hugo --destination `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/destination</span>

- Build a site, start up a webserver to serve it, and automatically reload when pages are edited:

`hugo server`
