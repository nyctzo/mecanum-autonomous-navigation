import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/nyctzo/dibyanshu_ws/install/my_first_pkg'
