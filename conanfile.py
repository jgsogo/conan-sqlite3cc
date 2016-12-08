
import os, shutil
from conans import ConanFile, CMake
from conans.tools import download, untargz


class SQLite3ccConan(ConanFile):
    name = "sqlite3cc"
    version = "0.1.1"
    requires = "sqlite3/3.15.2@jgsogo/stable",
    settings = "os", "compiler", "build_type", "arch"
    url = "https://github.com/jgsogo/conan-sqlite3cc"
    license = "GNU Lesser General Public License v.3"
    exports = ["FindSQLite3cc.cmake", "CMakeLists.txt", ]

    _build_dir = "build"
    
    @property
    def source_dir(self):
        return "{}-{}".format(self.name, self.version)

    def source(self):
        zip_name = '{}-{}.tar.xz'.format(self.name, self.version)
        url = 'http://ed.am/dev/sqlite3cc/{}'.format(zip_name)
        download(url, zip_name)

        import tarfile
        import pylzma
        import contextlib
        with contextlib.closing(pylzma.LZMAFile(zip_name)) as xz:
            with tarfile.open(fileobj=xz) as f:
                f.extractall('.')

        #untargz(zip_name)
        os.unlink(zip_name)

    def build(self):
        cmake = CMake(self.settings)
        shutil.move("CMakeLists.txt", "%s/CMakeLists.txt" % self.source_dir)
        self.run("mkdir {}".format(self._build_dir))

        cmake_command = 'cd {} && cmake {} {}'.format(self._build_dir, os.path.join("..", self.source_dir), cmake.command_line)
        self.output.info(cmake_command)
        self.run(cmake_command)

        build_command = "cd {} && cmake --build . {}".format(self._build_dir, cmake.build_config)
        self.output.info(build_command)
        self.run(build_command)

    def package(self):
        self.copy("FindSQLite3cc.cmake", ".", ".")
        self.copy("*.h", dst="include", src=os.path.jioin(self.source_dir, "include"))
        if self.settings.os == "Windows":
            self.copy(pattern="*.lib", dst="lib", src=self._build_dir, keep_path=False)
            self.copy(pattern="*.dll", dst="bin", src=self._build_dir, keep_path=False)
        else:
            self.copy(pattern="*.a", dst="lib", src=self._build_dir, keep_path=False)
            self.copy(pattern="*.lib", dst="lib", src=self._build_dir, keep_path=False)
            self.copy(pattern="*.pdb", dst="lib", src=self._build_dir, keep_path=False)

    def package_info(self):
        self.cpp_info.libs.append("sqlite3cc")
        if not self.settings.os == "Windows":
            self.cpp_info.libs.append("pthread")
            self.cpp_info.libs.append("dl")

