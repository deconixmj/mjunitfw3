#!D:\Py_projects\mjunitfw3_testsuite_nose\venv\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'unittest-parallel==1.0.5','console_scripts','unittest-parallel'
__requires__ = 'unittest-parallel==1.0.5'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('unittest-parallel==1.0.5', 'console_scripts', 'unittest-parallel')()
    )
