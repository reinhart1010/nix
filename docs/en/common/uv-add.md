---
layout: page
title: common/uv-add (English)
description: "Add package dependencies to the `pyproject.toml` file."
content_hash: 40e7feb738e899134ade659bcf9eb05f012c4cae
last_modified_at: 2025-03-02
related_topics:
  - title: español version
    url: /es/common/uv-add.html
    icon: bi bi-globe
tldri18n_status: 2
---
# uv add

Add package dependencies to the `pyproject.toml` file.
Packages are specified according to <https://peps.python.org/pep-0508/>.
More information: <https://docs.astral.sh/uv/reference/cli/#uv-add>.

- Add the latest version of a package:

`uv add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- Add multiple packages:

`uv add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package1 package2 ...</span>

- Add a package with a version requirement:

`uv add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package>=1.2.3</span>

- Add packages to an optional dependency group, which will be included when published:

`uv add --optional `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">optional</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package1 package2 ...</span>

- Add packages to a local group, which will not be included when published:

`uv add --group `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">group</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package1 package2 ...</span>

- Add packages to the dev group, shorthand for `--group dev`:

`uv add --dev `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package1 package2 ...</span>

- Add package as editable:

`uv add --editable `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/package/</span>

- Enable an extra when installing package, may be provided multiple times:

`uv add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>` --extra `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">extra_feature</span>
