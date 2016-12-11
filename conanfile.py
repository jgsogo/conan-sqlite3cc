
import os, shutil, sys
from conans import ConanFile, CMake
from conans.tools import download, untargz


class SQLite3ccConan(ConanFile):
    name = "sqlite3cc"
    version = "0.1.1"
    settings = "os", "compiler", "build_type", "arch"
    url = "https://github.com/jgsogo/conan-sqlite3cc"
    license = "GNU Lesser General Public License v.3"
    exports = ["FindSQLite3cc.cmake", "CMakeLists.txt", ]
    generators = "cmake"
    
    _build_dir = "build"
    
    def requirements(self):
        self.requires.add("Boost/1.60.0@lasote/stable")
        self.requires.add("sqlite3/3.15.2@jgsogo/stable")

    @property
    def source_dir(self):
        return "{}-{}".format(self.name, self.version)

    def source(self):
        zip_name = '{}-{}.tar.gz'.format(self.name, self.version)
        url = 'http://ed.am/dev/sqlite3cc/{}'.format(zip_name)
        download(url, zip_name)
        untargz(zip_name)
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
        
        # Run tests, always
        if self.settings.os == "Windows":
            command = "cd {} && test_blob.exe && test_main.exe".format(os.path.join(self._build_dir, "bin"))
        else:
            command = "cd {} && ./test_blog && ./test_main".format(os.path.join(self._build_dir, "bin"))
        self.output.info(command)
        self.run(command)

    def package(self):
        self.copy("FindSQLite3cc.cmake", ".", ".")
        self.copy("*.h", dst="include", src=os.path.join(self.source_dir, "include"))
        if self.settings.os == "Windows":
            self.copy(pattern="*.lib", dst="lib", src=self._build_dir, keep_path=False)
            self.copy(pattern="*.dll", dst="bin", src=self._build_dir, keep_path=False)
            self.copy(pattern="*.pdb", dst="lib", src=self._build_dir, keep_path=False)
        else:
            self.copy(pattern="*.a", dst="lib", src=self._build_dir, keep_path=False)
            self.copy(pattern="*.lib", dst="lib", src=self._build_dir, keep_path=False)

    def package_info(self):
        self.cpp_info.libs.append("sqlite3cc")
        if not self.settings.os == "Windows":
            self.cpp_info.libs.append("pthread")
            self.cpp_info.libs.append("dl")

