---
layout: page
title: common/license (English)
description: "Create license files for open-source projects."
content_hash: 6d3546bef5bdc333f26abe6c710cf4b69d10e5b9
last_modified_at: 2022-12-06
---
# license

Create license files for open-source projects.
More information: <https://nishanths.github.io/license>.

- Print a license to `stdout`, using the defaults (auto-detected author name, and current year):

`license `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">license_name</span>

- Generate a license and save it to a file:

`license -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">license_name</span>

- List all available licenses:

`license ls`

- Generate a license with custom author name and year:

`license --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">author</span>` --year `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">release_year</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">license_name</span>
