---
layout: page
title: common/license (English)
description: "Create license files for open-source projects."
content_hash: 7d147f64cf88555b865cafec602acd0dc82d1eed
last_modified_at: 2022-12-04
---
# license

Create license files for open-source projects.
More information: <https://nishanths.github.io/license>.

- Print a license to `stdout`, using the defaults (auto-detected author name, and current year):

`license `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">license_name</span>

- Generate a license and save it to a file:

`license -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filename</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">license_name</span>

- List all available licenses:

`license ls`

- Generate a license with custom author name and year:

`license --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">author</span>` --year `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">release_year</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">license_name</span>
