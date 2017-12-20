# BMO TEST PROJECT

*Version: 0.1*

## How to get started on your local development environment.
### Prerequisites:

program | download link
--- | ---
git | https://git-scm.com/downloads
python 2.7.x | https://www.python.org/downloads/

### Create project directory and environment

* `mkdir bmo_project && cd bmo_project`

*Obtain source code and clone into code directory*

* `git clone https://github.com/lestrato/bmo.git .`

*Your Directory structure will look like this:*
```
bmo
├── test_files (dir)
├── __init__.py
├── errors.py
├── graph_utils.py
├── LOGFILE.txt
├── part_1.py
├── part_2.py
├── part_3.py
├── README.md
├── tests.py

```

### To build your graph
1. run ```file_to_edgeset``` in ```graph_utils.py``` to convert a file to a graph dict object

### To run the supplied tests
1. ```python tests.py```

### To run a subproblem
1. you can run one of three files with this graph (and additional arguments):
* ```part_1.py``` (covers questions 1-5)
* ```part_2.py``` (covers questions 6, 7, 10)
* ```part_3.py``` (covers questions 8-9)
2. for examples on how to run these commands, see ```tests.py```
