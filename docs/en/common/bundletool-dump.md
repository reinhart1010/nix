---
layout: page
title: common/bundletool-dump (English)
description: "Manipulate Android Application Bundles."
content_hash: fae6508b2fc323f61ed7532ac3c2d54bb11bfd6a
last_modified_at: 2024-02-15
tldri18n_status: 2
---
# bundletool dump

Manipulate Android Application Bundles.
More information: <https://developer.android.com/studio/command-line/bundletool>.

- Display the `AndroidManifest.xml` of the base module:

`bundletool dump manifest --bundle=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/bundle.aab</span>

- Display a specific value from the `AndroidManifest.xml` using XPath:

`bundletool dump manifest --bundle=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/bundle.aab</span>` --xpath=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/manifest/@android:versionCode</span>

- Display the `AndroidManifest.xml` of a specific module:

`bundletool dump manifest --bundle=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/bundle.aab</span>` --module=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>

- Display all the resources in the application bundle:

`bundletool dump resources --bundle=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/bundle.aab</span>

- Display the configuration for a specific resource:

`bundletool dump resources --bundle=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/bundle.aab</span>` --resource=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">type/name</span>

- Display the configuration and values for a specific resource using the ID:

`bundletool dump resources --bundle=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/bundle.aab</span>` --resource=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0x7f0e013a</span>` --values`

- Display the contents of the bundle configuration file:

`bundletool dump config --bundle=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/bundle.aab</span>
