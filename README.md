django-project-template
====

This is a cookiecutter template for new django projects.

What does it do? (on top of django-admin startproject)
---
* Secrets (and some configuration) are fetched from environment variables
* Secret key, in addition to being specified with environment variables,
  can be generated and saved to a file on a per instance basis.
* Additional settings files for mysql databases, and running on Cloud9.
* Optional SSL proxy header checking
