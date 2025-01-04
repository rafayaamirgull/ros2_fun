import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/rafay/Documents/rafay/MyFolder_other_stuff/WSL_and_Stuff/other/open_source/ros2_fun/pub_sub_python3/install/pub_sub_python'
