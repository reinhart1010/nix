---
layout: page
title: common/abduco (English)
description: "Terminal session manager."
content_hash: 54f279c53cf0b4a9cfe29d4a6a3145ce43eefadd
related_topics:
  - title: italiano version
    url: /it/common/abduco.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/abduco.html
    icon: bi bi-globe
  - title: norsk bokmål (Norge) version
    url: /no/common/abduco.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/abduco.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/abduco.html
    icon: bi bi-globe
---
# abduco

Terminal session manager.
More information: <http://www.brain-dump.org/projects/abduco/>.

- List sessions:

`abduco`

- Attach to a session, creating it if it doesn't exist:

`abduco -A `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bash</span>

- Attach to a session with `dvtm`, creating it if it doesn't exist:

`abduco -A `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>

- Detach from a session:

`Ctrl + \`

- Attach to a session in read-only mode:

`abduco -Ar `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>
