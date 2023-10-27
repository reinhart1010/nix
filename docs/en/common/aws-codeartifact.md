---
layout: page
title: common/aws-codeartifact (English)
description: "CLI for AWS CodeArtifact."
content_hash: 3b8e155e531ac1aab10e72624acd3d6f7da4c8bd
last_modified_at: 2023-10-26
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># aws codeartifact

CLI for AWS CodeArtifact.
CodeArtifact allows you to store artifacts using popular package managers and build tools like Maven, Gradle, npm, Yarn, Twine, pip, NuGet, and SwiftPM.
More information: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeartifact/index.html>.

- List available domains for your AWS account:

`aws codeartifact list-domains`

- Generate credentials for a specific package manager (e.g.: npm, pip):

`aws codeartifact login --tool `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package_manager</span>` --domain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">your_domain</span>` --repository `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">repository_name</span>

- Get the endpoint URL of a CodeArtifact repository:

`aws codeartifact get-repository-endpoint --domain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">your_domain</span>` --repository `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">repository_name</span>` --format `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">npm|pypi|maven|nuget|generic</span>

- Show list of all available CodeArtifact commands:

`aws codeartifact help`

- Show help for specific EC2 subcommand:

`aws ec2 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">subcommand</span>` help`