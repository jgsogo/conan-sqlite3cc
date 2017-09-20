# Conan-SQLite3cc

This is just a [conan.io](http://conan.io) recipe for [sqlite3cc](http://ed.am/dev/sqlite3cc) library.


## Branches

There are several branches on this repo:

* **master**: it's linked against jgsogo's master branch at Launchpad [here](https://code.launchpad.net/~jgsogo/sqlite3cc/master)). Last sources available are downloaded and compiled every time the recipe is used.
  Write a ``conanfile.txt``:

  ```
     [requires]
     sqlite3cc/master@jgsogo/stable
  ```
 
* **release/x.y.z**: uses Tim Marston's released package with the same numbering [here](http://ed.am/dev/sqlite3cc) ([changelog](http://ed.am/dev/sqlite3cc/NEWS)).
  
  Write a ``conanfile.txt``:
 
  ```
     [requires]
     sqlite3cc/x.y.z@jgsogo/stable
  ```

It is recommended to use the Tim Marston last official release.


## Build status

<table>
    <thead>
        <tr>
            <th></th>
            <th colspan="3">Windows</th>
            <th colspan="4">Unix</th>
            <th>Macos</th>
        </tr>
    </thead>
    <tr>
        <td></td>
        <td>msvc 12</td>
        <td>msvc 14</td>
        <td>msvc 15</td>
        <td>gcc 4.9</td>
        <td>gcc 5.4</td>
        <td>gcc 6.3</td>
        <td>clang 4.0</td>
        <td>apple-clang 8.1</td>
    </tr>
    <tr>
        <td>master</td>
        <td><a href="https://ci.appveyor.com/project/jgsogo/conan-sqlite3cc"><img src="https://appveyor-matrix-badges.herokuapp.com/repos/jgsogo/conan-sqlite3cc/branch/master/1" alt="Build status"/></a></td>        
        <td><a href="https://ci.appveyor.com/project/jgsogo/conan-sqlite3cc"><img src="https://appveyor-matrix-badges.herokuapp.com/repos/jgsogo/conan-sqlite3cc/branch/master/2" alt="Build status"/></a></td>        
        <td><a href="https://ci.appveyor.com/project/jgsogo/conan-sqlite3cc"><img src="https://appveyor-matrix-badges.herokuapp.com/repos/jgsogo/conan-sqlite3cc/branch/master/3" alt="Build status"/></a></td>        
        <td><a href="https://travis-ci.org/jgsogo/conan-sqlite3cc"><img src="https://travis-matrix-badges.herokuapp.com/repos/jgsogo/conan-sqlite3cc/branches/master/1" alt="Build status"/></a></td>
        <td><a href="https://travis-ci.org/jgsogo/conan-sqlite3cc"><img src="https://travis-matrix-badges.herokuapp.com/repos/jgsogo/conan-sqlite3cc/branches/master/2" alt="Build status"/></a></td>
        <td><a href="https://travis-ci.org/jgsogo/conan-sqlite3cc"><img src="https://travis-matrix-badges.herokuapp.com/repos/jgsogo/conan-sqlite3cc/branches/master/3" alt="Build status"/></a></td>
        <td><a href="https://travis-ci.org/jgsogo/conan-sqlite3cc"><img src="https://travis-matrix-badges.herokuapp.com/repos/jgsogo/conan-sqlite3cc/branches/master/4" alt="Build status"/></a></td>
        <td><a href="https://travis-ci.org/jgsogo/conan-sqlite3cc"><img src="https://travis-matrix-badges.herokuapp.com/repos/jgsogo/conan-sqlite3cc/branches/master/5" alt="Build status"/></a></td>
    </tr>
    <tr>
        <td>release/0.1.1</td>
        <td><a href="https://ci.appveyor.com/project/jgsogo/conan-sqlite3cc"><img src="https://appveyor-matrix-badges.herokuapp.com/repos/jgsogo/conan-sqlite3cc/branch/release/0.1.1/1" alt="Build status"/></a></td>        
        <td><a href="https://ci.appveyor.com/project/jgsogo/conan-sqlite3cc"><img src="https://appveyor-matrix-badges.herokuapp.com/repos/jgsogo/conan-sqlite3cc/branch/release/0.1.1/2" alt="Build status"/></a></td>        
        <td><a href="https://ci.appveyor.com/project/jgsogo/conan-sqlite3cc"><img src="https://appveyor-matrix-badges.herokuapp.com/repos/jgsogo/conan-sqlite3cc/branch/release/0.1.1/3" alt="Build status"/></a></td>        
        <td><a href="https://travis-ci.org/jgsogo/conan-sqlite3cc"><img src="https://travis-matrix-badges.herokuapp.com/repos/jgsogo/conan-sqlite3cc/branches/release/0.1.1/1" alt="Build status"/></a></td>
        <td><a href="https://travis-ci.org/jgsogo/conan-sqlite3cc"><img src="https://travis-matrix-badges.herokuapp.com/repos/jgsogo/conan-sqlite3cc/branches/release/0.1.1/2" alt="Build status"/></a></td>
        <td><a href="https://travis-ci.org/jgsogo/conan-sqlite3cc"><img src="https://travis-matrix-badges.herokuapp.com/repos/jgsogo/conan-sqlite3cc/branches/release/0.1.1/3" alt="Build status"/></a></td>
        <td><a href="https://travis-ci.org/jgsogo/conan-sqlite3cc"><img src="https://travis-matrix-badges.herokuapp.com/repos/jgsogo/conan-sqlite3cc/branches/release/0.1.1/4" alt="Build status"/></a></td>
        <td><a href="https://travis-ci.org/jgsogo/conan-sqlite3cc"><img src="https://travis-matrix-badges.herokuapp.com/repos/jgsogo/conan-sqlite3cc/branches/release/0.1.1/5" alt="Build status"/></a></td>
    </tr>
</table>

* Build status for branch `release/0.1.1` is waiting for [this issue](https://github.com/bjfish/travis-matrix-badges/issues/8).


## License

[MIT LICENSE](./LICENSE)
 
