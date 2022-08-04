---
layout: page
title: osx/open (English)
description: "Opens files, directories and applications."
content_hash: 50222ece761a0e99789f5b6cee62f97b9c76aac9
related_topics:
  - title: Deutsch version
    url: /de/osx/open.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/open.html
    icon: bi bi-globe
---
# open

Opens files, directories and applications.
More information: <https://ss64.com/osx/open.html>.

- Open a file with the associated application:

`open `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file.ext</span>

- Run a graphical macOS application:

`open -a "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Application</span>`"`

- Run a graphical macOS app based on the bundle identifier (refer to `osascript` for an easy way to get this):

`open -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">com.domain.application</span>

- Open the current directory in Finder:

`open .`

- Reveal a file in Finder:

`open -R `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Open all the files of a given extension in the current directory with the associated application:

`open `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.ext</span>
