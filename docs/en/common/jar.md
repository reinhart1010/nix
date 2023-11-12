---
layout: page
title: common/jar (English)
description: "Java applications/libraries packager."
content_hash: e2fa80bcfc0e15c15c014ace04f23989dce8d1ac
last_modified_at: 2023-11-12
related_topics:
  - title: 한국어 version
    url: /ko/common/jar.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/jar.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/jar.html
    icon: bi bi-globe
tldri18n_status: 2
---
# jar

Java applications/libraries packager.
More information: <https://docs.oracle.com/javase/tutorial/deployment/jar/basicsindex.html>.

- Recursively archive all files in the current directory into a .jar file:

`jar cf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file.jar</span>` *`

- Unzip .jar/.war file to the current directory:

`jar -xvf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file.jar</span>

- List a .jar/.war file content:

`jar tf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.jar</span>

- List a .jar/.war file content with verbose output:

`jar tvf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.jar</span>
