[app]
title = LiteBrowser
package.name = litebrowser
package.domain = org.example
source.dir = .
source.include_exts = py,kv,png,jpg,xml
version = 1.0
requirements = python3,kivy
orientation = portrait
fullscreen = 0

# No INTERNET permission is requested.
android.permissions =
android.api = 35
android.minapi = 23
android.archs = arm64-v8a, armeabi-v7a

# Adds HTTP/HTTPS VIEW intent filters to the app's main PythonActivity.
android.manifest.intent_filters = ./android/browser_intent_filters.xml

[buildozer]
log_level = 2
warn_on_root = 1
