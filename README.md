# cyclic-voltammetry

Stremlit App to explore the data in the [echemdb repository](https://github.com/echemdb/electrochemistry-data), containing cyclic voltammograms (CVs) for single crystal electrodes.

A static version of the database can be found on [echemdb.org/cv](https://www.echemdb.org/cv/).

## Installation

### Install with pip

```sh
pip install -r requirements.txt
```

Continue below (Download the database).

### Developers

Clone the repository.

```sh
git clone git@github.com:DunklesArchipel/cyclic-voltammetry.git
cd cyclic-voltammetry
```

Install dependencies with conda (or mamba).

```sh
mamba env create -f environment.yaml
mamba activate echemdb_app
```

### Download the database

```sh
python
from unitpackage.collection import Collection
db = Collection.from_remote() # the download may take a few minutes
db.save_entries('entries')
exit()
```

## Run app

Execute

```sh
streamlit run app.py
```
