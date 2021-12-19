---
layout: page
title: common/git-request-pull (English)
description: "Generate a request asking the upstream project to pull changes into its tree."
content_hash: f426a780ab14103984b22de48e3de54b9f26eb9f
related_topics:
  - title: français version
    url: /fr/common/git-request-pull.html
    icon: bi bi-globe
---
# git request-pull

Generate a request asking the upstream project to pull changes into its tree.
More information: <https://git-scm.com/docs/git-request-pull>.

- Produce a request summarizing the changes between the v1.1 release and a specified branch:

`git request-pull `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">v1.1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com/project</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">branch_name</span>

- Produce a request summarizing the changes between the v0.1 release on the `foo` branch and the local `bar` branch:

`git request-pull `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">v0.1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com/project</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">foo:bar</span>
