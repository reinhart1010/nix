---
layout: page
title: common/bundletool (English)
description: "Command-line tool to manipulate Android Application Bundles."
content_hash: f7f9f3cefbad7d24c403701820bf9d5cf6f17d1b
---
# bundletool

Command-line tool to manipulate Android Application Bundles.
Some subcommands such as `bundletool validate` have their own usage documentation.
More information: <https://developer.android.com/studio/command-line/bundletool>.

- Display help for a subcommand:

`bundletool help `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">subcommand</span>

- Generate APKs from an application bundle (prompts for keystore password):

`bundletool build-apks --bundle=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/bundle.aab</span>` --ks=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/key.keystore</span>` --ks-key-alias=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">key_alias</span>` --output=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.apks</span>

- Generate APKs from an application bundle giving the keystore password:

`bundletool build-apks --bundle=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/bundle.aab</span>` --ks=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/key.keystore</span>` --ks-key-alias=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">key_alias</span>` –ks-pass=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pass:the_password</span>` --output=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.apks</span>

- Generate APKs including only one single APK for universal usage:

`bundletool build-apks --bundle=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/bundle.aab</span>` --mode=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">universal</span>` --ks=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/key.keystore</span>` --ks-key-alias=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">key_alias</span>` --output=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.apks</span>

- Install the right combination of APKs to an emulator or device:

`bundletool install-apks --apks=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.apks</span>

- Estimate the download size of an application:

`bundletool get-size total --apks=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.apks</span>

- Generate a device specification JSON file for an emulator or device:

`bundletool get-device-spec --output=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.json</span>

- Verify a bundle and display detailed information about it:

`bundletool validate --bundle=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/bundle.aab</span>
