---
layout: page
title: common/rails-routes (English)
description: "List routes in a Rails application."
content_hash: 2a77e5087f9f96965f8b79c75d1558427c9314df
related_topics:
  - title: Indonesia version
    url: /id/common/rails-routes.html
    icon: bi bi-globe
---
# rails routes

List routes in a Rails application.
More information: <https://guides.rubyonrails.org/routing.html>.

- List all routes:

`rails routes`

- List all routes in an expanded format:

`rails routes --expanded`

- List routes partially matching URL helper method name, HTTP verb, or URL path:

`rails routes -g `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">posts_path|GET|/posts</span>

- List routes that map to a specified controller:

`rails routes -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">posts|Posts|Blogs::PostsController</span>
