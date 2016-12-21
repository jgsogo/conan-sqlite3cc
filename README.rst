Conan-SQLite3cc
===============

This is just a `conan.io  <http://conan.io>`__ recipe for `sqlite3cc <http://ed.am/dev/sqlite3cc>`__ library.

+------------------------+----------------------+
| **master (linux/osx)** | **master (windows)** |
+========================+======================+
| |Build travis|         | |Build appveyor|     |
+------------------------+----------------------+

.. |Build travis| image:: https://travis-ci.org/jgsogo/conan-sqlite3cc.svg?branch=master
   :target: https://travis-ci.org/jgsogo/conan-sqlite3cc
.. |Build appveyor| image:: https://ci.appveyor.com/api/projects/status/ppgdurgjt3jqfrpj/branch/master?svg=true
   :target: https://ci.appveyor.com/project/jgsogo/conan-sqlite3cc/branch/master


Branches
--------

There are several branches on this repo:

* **master**: it's linked against jgsogo's master branch at Launchpad (`here <https://code.launchpad.net/~jgsogo/sqlite3cc/master>`__). Last sources available are downloaded and compiled every time the recipe is used.
  Write a ``conanfile.txt``:

  .. code-block::

     [requires]
     sqlite3cc/master@jgsogo/stable
 
* **release/x.y.z**: uses Tim Marston's relesed package with the same numbering (`here <http://ed.am/dev/sqlite3cc>`__) (`changelog <http://ed.am/dev/sqlite3cc/NEWS>`__).
 
  +----------------------+------------------------+--------------------------+
  | **release/x.y.z**    | **linux/osx**          | **windows**              |
  +======================+========================+==========================+
  | release/0.1.1        | |travis release/0.1.1| | |appveyor release/0.1.1| |
  +----------------------+------------------------+--------------------------+
 
  Write a ``conanfile.txt``:
 
  .. code-block::
 
     [requires]
     sqlite3cc/x.y.z@jgsogo/stable

It is recommended to use the Tim Marston last official release.


.. |travis release/0.1.1| image:: https://travis-ci.org/jgsogo/conan-sqlite3cc.svg?branch=release%2F0.1.1
   :target: https://travis-ci.org/jgsogo/conan-sqlite3cc/branches
.. |appveyor release/0.1.1| image:: https://ci.appveyor.com/api/projects/status/ppgdurgjt3jqfrpj/branch/release/0.1.1?svg=true
   :target: https://ci.appveyor.com/project/jgsogo/conan-sqlite3cc/history


License
-------

`MIT LICENSE <./LICENSE>`__
 
