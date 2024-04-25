---
layout: page
title: common/quarkus (English)
description: "Create Quarkus projects, manage extensions and perform essential build and development tasks."
content_hash: b4a3686453c058a3b398732dd9fc9a8366913fee
last_modified_at: 2024-04-25
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/quarkus.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># quarkus

Create Quarkus projects, manage extensions and perform essential build and development tasks.
More information: <https://quarkus.io/guides/cli-tooling>.

- Create a new application project in a new directory:

`quarkus create app `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">project_name</span>

- Run the current project in live coding mode:

`quarkus dev`

- Run the application:

`quarkus run`

- Run the current project in continuous testing mode:

`quarkus test`

- Add one or more extensions to the current project:

`quarkus extension add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">extension_name_1 extension_name_2 ...</span>

- Build a container image using Docker:

`quarkus image build docker`

- Deploy the application to Kubernetes:

`quarkus deploy kubernetes`

- Update project:

`quarkus update`
