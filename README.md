# CFL
![Size of the repo](https://img.shields.io/github/repo-size/Vinz2008/cfl)
[![Number of commits in a year](https://img.shields.io/github/commit-activity/y/Vinz2008/cfl)](https://github.com/Vinz2008/cfl/commits/main)
[![Testing in github actions](https://img.shields.io/github/workflow/status/Vinz2008/cfl/Cfl%20tests)](https://github.com/Vinz2008/cfl/actions/workflows/tests.yml)

## Meaning of CFL
CFL mean calculation Function Language  
(It is more an interpreter but I think that CFL is a better name than CFI)
## About CFL
CFL is a mathematical interpreter that can interpret calculations like additions. You just need to type for example 1 + 1 and It will print 2. 
## Developping
### Adding operations 
If you want to add an operation, you need to :
<ol>
  <li>Add a python file that you name like you want in operation/files</li>
  <li>Put a function for the operation in this file with two numbers that are in this function and wich return the total of the operation Ex: def mult(nb1,nb2)</li>
  <li>Run the fusion.sh bash script</li>
  <li>Add an if for the character which will be used for your operation in the function operations and in the for loop in the other.py Ex: if i == "*"</li>
  
</ol>

## Limitations
For now, you can have only one operation to do each time like an addition.  
1 + 1 * 2 ❌  
1 * 2 ✅  
