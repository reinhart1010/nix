---
layout: page
title: common/bundle (English)
description: "Dependency manager for the Ruby programming language."
content_hash: 2f257c1e41cbe806ce6dd09ad226301e06cd2d92
last_modified_at: 2023-12-03
related_topics:
  - title: français version
    url: /fr/common/bundle.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/bundle.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/bundle.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/bundle.html
    icon: bi bi-globe
tldri18n_status: 2
---
# bundle

Dependency manager for the Ruby programming language.
More information: <https://bundler.io/man/bundle.1.html>.

- Install all gems defined in the `Gemfile` expected in the working directory:

`bundle install`

- Execute a command in the context of the current bundle:

`bundle exec `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arguments</span>

- Update all gems by the rules defined in the `Gemfile` and regenerate `Gemfile.lock`:

`bundle update`

- Update one or more specific gem(s) defined in the `Gemfile`:

`bundle update `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gem_name1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gem_name2</span>

- Update one or more specific gems(s) defined in the `Gemfile` but only to the next patch version:

`bundle update --patch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gem_name1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gem_name2</span>

- Update all gems within the given group in the `Gemfile`:

`bundle update --group `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">development</span>

- List installed gems in the `Gemfile` with newer versions available:

`bundle outdated`

- Create a new gem skeleton:

`bundle gem `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gem_name</span>
