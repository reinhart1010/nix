---
layout: page
title: common/rails-generate (English)
description: "Generate new Rails templates in an existing project."
content_hash: f75ecaa415090809233cf04e3018d4ee8ee2fa0b
last_modified_at: 2023-11-12
related_topics:
  - title: Indonesia version
    url: /id/common/rails-generate.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/rails-generate.html
    icon: bi bi-globe
tldri18n_status: 2
---
# rails generate

Generate new Rails templates in an existing project.
More information: <https://guides.rubyonrails.org/command_line.html#bin-rails-generate>.

- List all available generators:

`rails generate`

- Generate a new model named Post with attributes title and body:

`rails generate model `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Post</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">title:string</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">body:text</span>

- Generate a new controller named Posts with actions index, show, new and create:

`rails generate controller `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Posts</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">index</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">show</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">new</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">create</span>

- Generate a new migration that adds a category attribute to an existing model called Post:

`rails generate migration `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">AddCategoryToPost</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">category:string</span>

- Generate a scaffold for a model named Post, predefining the attributes title and body:

`rails generate scaffold `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Post</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">title:string</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">body:text</span>
