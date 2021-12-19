---
layout: page
title: common/berks (English)
description: "Chef cookbook dependency manager."
content_hash: 9c21fb6569ca4abe74d9d39c89648505112dc909
related_topics:
  - title: italiano version
    url: /it/common/berks.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/berks.html
    icon: bi bi-globe
---
# berks

Chef cookbook dependency manager.
More information: <https://docs.chef.io/berkshelf.html>.

- Install cookbook dependencies into a local repo:

`berks install`

- Update a specific cookbook and its dependencies:

`berks update `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cookbook</span>

- Upload a cookbook to the Chef server:

`berks upload `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cookbook</span>

- View the dependencies of a cookbook:

`berks contingent `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cookbook</span>
