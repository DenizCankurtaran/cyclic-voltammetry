# Cyclic-voltammetry

Streamlit App to explore the data in the [echemdb repository](https://github.com/echemdb/electrochemistry-data), containing cyclic voltammograms (CVs) for single crystal electrodes.

A static version of the database can be found on [echemdb.org/cv](https://www.echemdb.org/cv/).

## Features

- Interactive periodic system to select elements
- Overview of all electrodes with various filter possibilities
- Display electrodes visualized inside a graph
- Normalize entries with various normalization functions and filters
- View detailed information of each individual electrode
- Easy to use interface

## Installation

### Developers

Clone the repository.

```sh
git clone git@github.com:DunklesArchipel/cyclic-voltammetry.git
cd cyclic-voltammetry
```
Note: You can install the requirements for this project with either pip OR conda (mamba). If you're using pip it's not necessary to use conda and the other way around

### Install with pip

```sh
pip install -r requirements.txt
```

### Install dependencies with conda (or mamba).

```sh
mamba env create -f environment.yaml
mamba activate echemdb_app
```

### Download the database

To properly use the applicaiton it's necessary to download the recent version of the database with the [unitpackage](https://echemdb.github.io/unitpackage/) API. Rerun the following lines, when the database changes.

```sh
python
from unitpackage.collection import Collection
db = Collection.from_remote() # the download may take a few minutes
db.save_entries('entries')
exit()
```

Alternatively, you can also run ```db\_persist_db_local.py ``` to download the database.

## Run app

Execute

```sh
streamlit run app.py
```
