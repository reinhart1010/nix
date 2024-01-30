---
layout: page
title: common/sonar-scanner (English)
description: "A generic scanner for SonarQube projects that do not use build tools such as Maven, Gradle, or Ant."
content_hash: 24872c652d5c8f2e3c473a9fe807802e42632d49
last_modified_at: 2024-01-30
tldri18n_status: 2
---
# sonar-scanner

A generic scanner for SonarQube projects that do not use build tools such as Maven, Gradle, or Ant.
More information: <https://docs.sonarqube.org/latest/analysis/scan/sonarscanner/>.

- Scan a project with configuration file in your project's root directory named `sonar-project.properties`:

`sonar-scanner`

- Scan a project using configuration file other than `sonar-project.properties`:

`sonar-scanner -D`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">project.settings=myproject.properties</span>

- Print debugging information:

`sonar-scanner -X`

- Display help:

`sonar-scanner -h`
