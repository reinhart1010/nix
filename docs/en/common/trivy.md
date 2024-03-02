---
layout: page
title: common/trivy (English)
description: "Scanner for vulnerabilities in container images, file systems, and Git repositories, as well as for configuration issues."
content_hash: 9cb196f0d27a12f3f5bb338b83cc396d791717ed
last_modified_at: 2024-03-02
tldri18n_status: 2
---
# trivy

Scanner for vulnerabilities in container images, file systems, and Git repositories, as well as for configuration issues.
More information: <https://aquasecurity.github.io/trivy>.

- Scan a Docker image for vulnerabilities and exposed secrets:

`trivy image `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image:tag</span>

- Scan a Docker image filtering the output by severity:

`trivy image --severity `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">HIGH,CRITICAL</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">alpine:3.15</span>

- Scan a Docker image ignoring any unfixed/unpatched vulnerabilities:

`trivy image --ignore-unfixed `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">alpine:3.15</span>

- Scan the filesystem for vulnerabilities and misconfigurations:

`trivy fs --security-checks `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vuln,config</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/project_directory</span>

- Scan a IaC (Terraform, CloudFormation, ARM, Helm and Dockerfile) directory for misconfigurations:

`trivy config `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/iac_directory</span>

- Scan a local or remote Git repository for vulnerabilities:

`trivy repo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/local_repository_directory|remote_repository_URL</span>

- Scan a Git repository up to a specific commit hash:

`trivy repo --commit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commit_hash</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">repository</span>

- Generate output with a SARIF template:

`trivy image --format `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">template</span>` --template `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">"@sarif.tpl"</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/report.sarif</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image:tag</span>
