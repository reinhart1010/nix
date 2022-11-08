---
layout: page
title: linux/virt-xml-validate (English)
description: "Validate `libvirt` XML files against a schema."
content_hash: 34aa7cc6e9d289417cbb6d80144a788c7461004a
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># virt-xml-validate

Validate `libvirt` XML files against a schema.
If a schema is not specified, the schema is determined by the root element in the XML file.
More information: <https://libvirt.org/manpages/virt-xml-validate.html>.

- Validate an XML file against a specific schema:

`virt-xml-validate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.xml</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">schema</span>

- Validate the domain XML against the domain schema:

`virt-xml-validate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/domain.xml</span>` domain`
