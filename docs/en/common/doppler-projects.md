---
layout: page
title: common/doppler-projects (English)
description: "Manage Doppler Projects."
content_hash: 7bc20e7c433e9df6dd9cc5ba9efefd4afb22b30b
last_modified_at: 2024-08-04
tldri18n_status: 2
---
# doppler projects

Manage Doppler Projects.
More information: <https://docs.doppler.com/docs/cli>.

- Get all projects:

`doppler projects`

- Get info for a project:

`doppler projects get `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name|project_id</span>

- Create a project:

`doppler projects create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>

- Update a project's name and description:

`doppler projects update `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name|project_id</span>` --name "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">new_name</span>`" --description "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">new_description</span>`"`

- Delete a project:

`doppler projects delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name|project_id</span>
