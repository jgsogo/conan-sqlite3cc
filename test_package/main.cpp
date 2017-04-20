#include <iostream>
#include <sqlite3cc.h>

int main(void)
{
    std::cout << "SQLite3cc " << sqlite3_libversion() << " succeeded!!" << std::endl;
    return 0;
}

