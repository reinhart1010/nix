---
layout: page
title: common/hadolint (English)
description: "Dockerfile linter."
content_hash: 5d804d2d868ad1b8a0bdb8db5569d523f8dd4fbe
last_modified_at: 2024-01-31
tldri18n_status: 2
---
# hadolint

Dockerfile linter.
More information: <https://github.com/hadolint/hadolint>.

- Lint a Dockerfile:

`hadolint `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/Dockerfile</span>

- Lint a Dockerfile, displaying the output in JSON format:

`hadolint --format `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">json</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/Dockerfile</span>

- Lint a Dockerfile, displaying the output in a specific format:

`hadolint --format `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tty|json|checkstyle|codeclimate|codacy</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/Dockerfile</span>

- Lint a Dockerfile ignoring specific rules:

`hadolint --ignore `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">DL3006</span>` --ignore `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">DL3008</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/Dockerfile</span>

- Lint multiple Dockerfiles using specific trusted registries:

`hadolint --trusted-registry `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">docker.io</span>` --trusted-registry `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5000</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/Dockerfile1 path/to/Dockerfile2 ...</span>
