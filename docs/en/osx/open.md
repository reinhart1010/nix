---
layout: page
title: osx/open (English)
description: "Opens files, directories and applications."
content_hash: d390dc12fb40b1f885b8ce3d88134e0b8e0faddf
last_modified_at: 2024-01-31
related_topics:
  - title: Deutsch version
    url: /de/osx/open.html
    icon: bi bi-globe
  - title: español version
    url: /es/osx/open.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/osx/open.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/open.html
    icon: bi bi-globe
tldri18n_status: 2
---
# open

Opens files, directories and applications.
More information: <https://keith.github.io/xcode-man-pages/open.1.html>.

- Open a file with the associated application:

`open `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file.ext</span>

- Run a graphical macOS [a]pplication:

`open -a "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Application</span>`"`

- Run a graphical macOS app based on the [b]undle identifier (refer to `osascript` for an easy way to get this):

`open -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">com.domain.application</span>

- Open the current directory in Finder:

`open .`

- [R]eveal a file in Finder:

`open -R `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Open all the files of a given extension in the current directory with the associated application:

`open `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.ext</span>

- Open a [n]ew instance of an application specified via [b]undle identifier:

`open -n -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">com.domain.application</span>
