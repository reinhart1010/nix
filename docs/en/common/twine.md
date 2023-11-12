---
layout: page
title: common/twine (English)
description: "Utility for publishing Python packages on PyPI."
content_hash: 7ad3db260997006b25605d26326dcf596fc66e0b
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# twine

Utility for publishing Python packages on PyPI.
More information: <https://twine.readthedocs.io/en/stable/#commands>.

- Upload to PyPI:

`twine upload dist/*`

- Upload to the Test PyPI [r]epository to verify things look right:

`twine upload -r testpypi dist/*`

- Upload to PyPI with a specified [u]sername and [p]assword:

`twine upload -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>` -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">password</span>` dist/*`

- Upload to an alternative repository URL:

`twine upload --repository-url `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">repository_url</span>` dist/*`

- Check that your distribution's long description should render correctly on PyPI:

`twine check dist/*`

- Upload using a specific pypirc configuration file:

`twine upload --config-file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">configuration_file</span>` dist/*`

- Continue uploading files if one already exists (only valid when uploading to PyPI):

`twine upload --skip-existing dist/*`

- Upload to PyPI showing detailed information:

`twine upload --verbose dist/*`
