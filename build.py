
import os
from conan.packager import ConanMultiPackager
from conanfile import SQLite3ccConan

username = os.getenv("CONAN_USERNAME", "jgsogo")
reference = os.getenv("CONAN_REFERENCE", "{}/{}".format(SQLite3ccConan.name, SQLite3ccConan.version))


if __name__ == "__main__":
    builder = ConanMultiPackager(username=username,
                                 reference=reference,
                                 visual_versions=["14",],
                                 gcc_versions = ["5.4", "6.3",],
                                 apple_clang_versions = ["7.3", "8.1",],
                                 stable_branch_pattern="master|release\/\d+\.\d+(\.\d+)?",
                                 args="--build=missing")
    builder.add_common_builds()
    builder.run()

