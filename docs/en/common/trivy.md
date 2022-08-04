---
layout: page
title: common/trivy (English)
description: "Scanner for vulnerabilities in container images, file systems, and Git repositories, as well as for configuration issues."
content_hash: 229e28e491fbea8e5b76c31b77db78829621cfe8
---
# trivy

Scanner for vulnerabilities in container images, file systems, and Git repositories, as well as for configuration issues.
More information: <https://github.com/aquasecurity/trivy>.

- Scan an image:

`trivy image `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image:tag</span>

- Scan the filesystem for vulnerabilities and misconfigurations:

`trivy fs --security-checks `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vuln,config</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/project_directory</span>

- Scan a directory for misconfigurations:

`trivy config `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/iac_directory</span>

- Generate output with a SARIF template:

`trivy image --format `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">template</span>` --template `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">"@sarif.tpl"</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/report.sarif</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image:tag</span>
