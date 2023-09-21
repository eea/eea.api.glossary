==========================
eea.api.glossary
==========================
.. image:: https://ci.eionet.europa.eu/buildStatus/icon?job=eea/eea.api.glossary/develop
  :target: https://ci.eionet.europa.eu/job/eea/job/eea.api.glossary/job/develop/display/redirect
  :alt: Develop
.. image:: https://ci.eionet.europa.eu/buildStatus/icon?job=eea/eea.api.glossary/master
  :target: https://ci.eionet.europa.eu/job/eea/job/eea.api.glossary/job/master/display/redirect
  :alt: Master

The eea.api.glossary is a Plone add-on

.. contents::


Main features
=============

1. Provides the vocabulary for the `volto-eea-slate-glossary <https://github.com/eea/volto-eea-slate-glossary>`_ addon


Install
=======

* Add eea.api.glossary to your eggs section in your buildout and
  re-run buildout::

    [buildout]
    eggs +=
      eea.api.glossary

* Or via docker::

    $ docker run --rm -p 8080:8080 -e ADDONS="eea.api.glossary" plone

* Install *eea.api.glossary* within Site Setup > Add-ons

Eggs repository
===============

- https://pypi.python.org/pypi/eea.api.glossary
- http://eggrepo.eea.europa.eu/simple


Plone versions
==============
It has been developed and tested for Plone 5.

How to contribute
=================
See the `contribution guidelines (CONTRIBUTING.md) <https://github.com/eea/eea.api.glossary/blob/master/CONTRIBUTING.md>`_.

Copyright and license
=====================

eea.api.glossary (the Original Code) is free software; you can
redistribute it and/or modify it under the terms of the
GNU General Public License as published by the Free Software Foundation;
either version 2 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but
WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY
or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License
for more details.

You should have received a copy of the GNU General Public License along
with this program; if not, write to the Free Software Foundation, Inc., 59
Temple Place, Suite 330, Boston, MA 02111-1307 USA.

The Initial Owner of the Original Code is European Environment Agency (EEA).
Portions created by Eau de Web are Copyright (C) 2009 by
European Environment Agency. All Rights Reserved.


Funding
=======

EEA_ - European Environment Agency (EU)

.. _EEA: https://www.eea.europa.eu/
.. _`EEA Web Systems Training`: http://www.youtube.com/user/eeacms/videos?view=1
