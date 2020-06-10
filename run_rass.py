import sys
import re

from rasa.__main__ import main

if __name__ == '__main__':
    [sys.argv.append(i) for i in ['run', 'actions', '-vv']]
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(main())