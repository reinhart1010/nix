---
layout: page
title: common/twine (English)
description: "Utility for publishing Python packages on PyPI."
content_hash: 85a3ca5f3ed2ca801c080b140cb31b176d774e9a
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># twine

Utility for publishing Python packages on PyPI.
Subcommands such as `twine upload` have their own usage documentation.
More information: <https://twine.readthedocs.io>.

- Upload to the Test PyPI [r]epository and verify things look right:

`twine upload -r testpypi dist/*`

- Upload to PyPI:

`twine upload dist/*`

- Upload to PyPI with a specified [u]sername and [p]assword:

`twine upload -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>` -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">password</span>` dist/*`

- Upload to an alternative repository URL:

`twine upload --repository-url `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">repository_url</span>` dist/*`
