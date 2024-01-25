---
layout: page
title: common/cs-fetch (English)
description: "Fetch fetches the JARs of dependencies."
content_hash: ad8d4ff4f217f44d8e35709fcba358cfa48b895b
last_modified_at: 2024-01-25
tldri18n_status: 2
---
# cs fetch

Fetch fetches the JARs of dependencies.
More information: <https://get-coursier.io/docs/cli-fetch>.

- Fetch a specific version of a jar:

`cs fetch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">group_id</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">artifact_id</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">artifact_version</span>

- Fetch a package and evaluate the classpath corresponding to the selected package in an env var:

`CP="$(cs fetch --classpath org.scalameta::scalafmt-cli:latest.release)"`

- Fetch a source of a specific jar:

`cs fetch --sources `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">group_id</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">artifact_id</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">artifact_version</span>

- Fetch the javadoc jars:

`cs fetch --javadoc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">group_id</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">artifact_id</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">artifact_version</span>

- Fetch dependency with javadoc jars and source jars:

`cs fetch --default=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">true</span>` --sources --javadoc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">group_id</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">artifact_id</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">artifact_version</span>

- Fetch jars coming from dependency files:

`cs fetch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">--dependency-file path/to/file1 --dependency-file path/to/file2 ...</span>
