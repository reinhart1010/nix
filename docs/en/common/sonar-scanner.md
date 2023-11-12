---
layout: page
title: common/sonar-scanner (English)
description: "SonarScanner is a generic scanner for SonarQube projects that do not use build tools such as Maven, Gradle, or Ant."
content_hash: bce8539b35acba9922906e3c6f3a131c6d4859db
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# sonar-scanner

SonarScanner is a generic scanner for SonarQube projects that do not use build tools such as Maven, Gradle, or Ant.
More information: <https://docs.sonarqube.org/latest/analysis/scan/sonarscanner/>.

- Scan a project with configuration file in your project's root directory named `sonar-project.properties`:

`sonar-scanner`

- Scan a project using configuration file other than `sonar-project.properties`:

`sonar-scanner -D`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">project.settings=myproject.properties</span>

- Print help information:

`sonar-scanner -h`

- Print debugging information:

`sonar-scanner -X`
