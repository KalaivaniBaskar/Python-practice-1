# modules is just a .py script thst you call in other .py scripts

#pkgs are collectin of modules 

from mymodule import my_func # import a module 
my_func() # running a fn from other module 

#in the above ex, we saw how to import a module in the same folder/pkg 

#lets see how use pkgs  and import from it

#folders should have a __init__.py file to be treated as a pkg
from MyPkg import main_script
from MyPkg.SubPkg import sub_script

main_script.main_script_fn()
sub_script.sub_report()
