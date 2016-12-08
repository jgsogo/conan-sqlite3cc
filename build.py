
import os
from conan.packager import ConanMultiPackager
from conanfile import SQLite3Conan

username = os.getenv("CONAN_USERNAME", "jgsogo")
reference = os.getenv("CONAN_REFERENCE", "{}/{}".format(SQLite3ccConan.name, SQLite3ccConan.version))


if __name__ == "__main__":
    builder = ConanMultiPackager(username=username, reference=reference)
    builder.add_common_builds()
    builder.run()

