FollowBot
========

Automated bot to favorite tweets!

Deployment
------------

Run this script: (TODO - automate this)

.. code-block:: python

    from django.contrib.sites.models import Site
    site = Site.objects.get()
    site.domain = "example.com"
    site.name = "followbot"
    site.save()
