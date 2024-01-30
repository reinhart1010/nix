---
layout: page
title: common/xml-validate (English)
description: "Validate XML documents."
content_hash: 7a18bf9269d535213c8cbbc4600eb04849b1938f
last_modified_at: 2024-01-30
tldri18n_status: 2
---
# xml validate

Validate XML documents.
More information: <http://xmlstar.sourceforge.net/docs.php>.

- Validate one or more XML documents for well-formedness only:

`xml validate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input1.xml|URI</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">input2.xml ...</span>

- Validate one or more XML documents against a Document Type Definition (DTD):

`xml validate --dtd `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/schema.dtd</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input1.xml|URI</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">input2.xml ...</span>

- Validate one or more XML documents against an XML Schema Definition (XSD):

`xml validate --xsd `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/schema.xsd</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input1.xml|URI</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">input2.xml ...</span>

- Validate one or more XML documents against a Relax NG schema (RNG):

`xml validate --relaxng `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/schema.rng</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input1.xml|URI</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">input2.xml ...</span>

- Display help:

`xml validate --help`
