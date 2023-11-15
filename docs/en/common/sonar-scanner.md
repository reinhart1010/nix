---
layout: page
title: common/sonar-scanner (English)
description: "A generic scanner for SonarQube projects that do not use build tools such as Maven, Gradle, or Ant."
content_hash: 67b3f89c49a64f39ea20b8c123714235c6ce32ee
last_modified_at: 2023-11-15
tldri18n_status: 2
---
# sonar-scanner

A generic scanner for SonarQube projects that do not use build tools such as Maven, Gradle, or Ant.
More information: <https://docs.sonarqube.org/latest/analysis/scan/sonarscanner/>.

- Scan a project with configuration file in your project's root directory named `sonar-project.properties`:

`sonar-scanner`

- Scan a project using configuration file other than `sonar-project.properties`:

`sonar-scanner -D`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">project.settings=myproject.properties</span>

- Print help information:

`sonar-scanner -h`

- Print debugging information:

`sonar-scanner -X`
