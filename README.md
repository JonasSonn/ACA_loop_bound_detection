# ACA_loop_bound_detection

Loop bound detection for tightening loop bounds by abstract execution.

Input: CFG file with data flow annotations:

- Loop iteration expression: a common loop iteration expression would be x : x+1. But can be extended to any function as long as the function doesn't create a infinite loop.
- Loop end condition : so far only classic conditions (x<100) are sure to work with the tool. 
- Abstract_store : The variables that you'd want to test on the loop. 

Output: Bounds on loops


Run the script by 
  
   python main.py '"path_to_cfg_file"'
   



