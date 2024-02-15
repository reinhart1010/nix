---
layout: page
title: common/aws-codeartifact (English)
description: "Manage CodeArtifact repositories, domains, packages, package versions and assets."
content_hash: 221f2a1a21afc32c85d6c6c7711c19013c599e8c
last_modified_at: 2024-02-15
related_topics:
  - title: português (Brasil) version
    url: /pt_BR/common/aws-codeartifact.html
    icon: bi bi-globe
tldri18n_status: 2
---
# aws codeartifact

Manage CodeArtifact repositories, domains, packages, package versions and assets.
CodeArtifact is an artifact repository compatible with popular package managers and build tools like Maven, Gradle, npm, Yarn, Twine, pip, NuGet, and SwiftPM.
More information: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeartifact/index.html>.

- List available domains for your AWS account:

`aws codeartifact list-domains`

- Generate credentials for a specific package manager:

`aws codeartifact login --tool `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">npm|pip|twine</span>` --domain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">your_domain</span>` --repository `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">repository_name</span>

- Get the endpoint URL of a CodeArtifact repository:

`aws codeartifact get-repository-endpoint --domain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">your_domain</span>` --repository `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">repository_name</span>` --format `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">npm|pypi|maven|nuget|generic</span>

- Display help:

`aws codeartifact help`

- Display help for a specific subcommand:

`aws codeartifact `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">subcommand</span>` help`
