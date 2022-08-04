---
layout: page
title: common/bundletool-dump (English)
description: "Command-line tool to manipulate Android Application Bundles."
content_hash: 1adfe9798bc4aaffe07b665cbf2cf286c3003e7f
---
# bundletool dump

Command-line tool to manipulate Android Application Bundles.
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
