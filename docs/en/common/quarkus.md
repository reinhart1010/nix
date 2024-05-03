---
layout: page
title: common/quarkus (English)
description: "Create Quarkus projects, manage extensions and perform essential build and development tasks."
content_hash: 1c4d97931808e45ca6de934aeb575b5d95cb265e
last_modified_at: 2024-05-03
tldri18n_status: 2
---
# quarkus

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

`quarkus extension add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">extension_name1 extension_name2 ...</span>

- Build a container image using Docker:

`quarkus image build docker`

- Deploy the application to Kubernetes:

`quarkus deploy kubernetes`

- Update project:

`quarkus update`
