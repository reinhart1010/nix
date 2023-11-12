---
layout: page
title: common/jenv (English)
description: "Command-line tool to manage the \"JAVA_HOME\" environment variable."
content_hash: 2a06a681879da363739e5e44afc7f797ddf6f361
last_modified_at: 2023-11-12
related_topics:
  - title: 中文 version
    url: /zh/common/jenv.html
    icon: bi bi-globe
tldri18n_status: 2
---
# jenv

Command-line tool to manage the "JAVA_HOME" environment variable.
More information: <https://www.jenv.be/>.

- Add a Java version to jEnv:

`jenv add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/jdk_home</span>

- Display the current JDK version used:

`jenv version`

- Display all managed JDKs:

`jenv versions`

- Set the global JDK version:

`jenv global `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">java_version</span>

- Set the JDK version for the current shell session:

`jenv shell `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">java_version</span>

- Enable a jEnv plugin:

`jenv enable-plugin `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">plugin_name</span>
