---
layout: page
title: common/gh-skyline (English)
description: "Generate a 3D model of your GitHub contribution history."
content_hash: 7e3e66934ebe34a6294448fef2f05d3c54eb15b5
last_modified_at: 2024-12-11
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/gh-skyline.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># gh skyline

Generate a 3D model of your GitHub contribution history.
By default, it will create a `{username}-{year}-github-skyline.stl` file in the current directory.
More information: <https://github.com/github/gh-skyline>.

- Generate a skyline STL file for the current year and authenticated user:

`gh skyline`

- Generate a skyline for a specific [u]ser and [y]ear:

`gh skyline --user `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>` --year `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">year</span>

- Generate a skyline for a range of [y]ears:

`gh skyline --user `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>` --year `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">first_year</span>`-`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">last_year</span>

- Generate a [f]ull skyline (from the user's join year to the current year):

`gh skyline --user `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>` --full`

- Enable [d]ebug logging:

`gh skyline --debug`

- Generate a skyline and specify the [o]utput file path:

`gh skyline --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output_file.stl</span>

- Open the GitHub profile for a specific [u]ser:

`gh skyline --user `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>` --web`

- Display [h]elp:

`gh skyline --help`
