# MapReduce Sample

This repository contains simple Python scripts to emulate a MapReduce work.


## Cloning the Repository

To get started, clone this repository by running the following command in your terminal:

```bash
git clone git@github.com:bigdatawirtz/mapreducesample.git
```

## Executing the code 

View the data

`cat datos.txt`

Map the data (output: key-value pairs)

`cat datos.txt | python mapper.py`

Sort the mapped data

`cat datos.txt | python mapper.py | sort ` 

Reduce the sorted data (output: key-value results)

`cat datos.txt | python mapper.py | sort | python reducer.py` 