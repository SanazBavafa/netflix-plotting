{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 108,
   "id": "44706332-a92f-4c98-a2d1-bc90036937c8",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(RowsNum,ColsNum): (8807, 12)\n",
      "\n",
      "Number of missing values in each column::\n",
      " show_id            0\n",
      "type               0\n",
      "title              0\n",
      "director        2634\n",
      "cast             825\n",
      "country          831\n",
      "date_added        10\n",
      "release_year       0\n",
      "rating             4\n",
      "duration           3\n",
      "listed_in          0\n",
      "description        0\n",
      "dtype: int64\n",
      "\n",
      "Number of duplicate rows: 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\khaled\\AppData\\Local\\Temp\\ipykernel_11212\\1852410757.py:46: UserWarning: Could not infer format, so each element will be parsed individually, falling back to `dateutil`. To ensure parsing is consistent and as-expected, please specify a format.\n",
      "  df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Saved cleaned to netflix-plotting/data/clean/netflix_clean.csv\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "import numpy as np\n",
    "import os\n",
    "# Using dateparser for cleaning 'date_added' column\n",
    "import dateparser\n",
    "\n",
    "os.makedirs(\"data/clean\", exist_ok=True)\n",
    "\n",
    "#read the csv file\n",
    "df = pd.read_csv(\"netflix-plotting/data/raw/netflix_titles.csv\")\n",
    "\n",
    "#Convert all columns to a single template for easy use\n",
    "df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')\n",
    "\n",
    "#Using shape method to see the amount of rows and columns in the dataframe\n",
    "print(f\"(RowsNum,ColsNum): {df.shape}\\n\")\n",
    "\n",
    "# Get the number of null values in each column\n",
    "print(f\"Number of missing values in each column::\\n {df.isnull().sum()}\\n\")\n",
    "\n",
    "#convert selected dataframe columns into string to apply strip method to remove any leading and trailing whitespaces from the values of that columns\n",
    "df['title'] = df['title'].astype(str).str.strip()\n",
    "df['type']  = df['type'].astype(str).str.strip().str.title()  # Movie / Tv Show\n",
    "df['country']  = df['country'].astype(str).str.strip().str.title()\n",
    "df['listed_in']  = df['listed_in'].astype(str).str.strip().str.title() \n",
    "\n",
    "#Convert the \"release_year\" column into int and it's null values to NaN\n",
    "df['release_year'] = pd.to_numeric(df['release_year'], errors='coerce').astype('Int64')\n",
    "\n",
    "# Splitting \"duration\" column into two separate columns:\n",
    "df['duration_num'] = df['duration'].astype(str).str.extract(r'(\\d+)').astype(float) #\"duration_num\": numeric value (e.g., 90, 2)\n",
    "df['duration_type'] = df['duration'].astype(str).str.extract(r'([A-Za-z]+)')[0].fillna('') #\"duration_type\": unit/type (e.g., min, Seasons)\n",
    "\n",
    "# Cleaning and transforming \"country\",\"listed_in\" columns:\n",
    "df['country'] = df['country'].fillna('') #Replace missing values with empty string\n",
    "df['listed_in'] = df['listed_in'].fillna('')\n",
    "\n",
    "#df['country_str'] = df['country'].str.replace(r'\\s*,\\s*', ', ', regex=True).fillna('')#Split countries by ','\n",
    "#df['genre_str'] = df['listed_in'].str.replace(r'\\s*,\\s*', ', ', regex=True).fillna('')#Split listed_in by ','\n",
    "\n",
    "#df['country_list'] = df['country'].str.split(',').apply(lambda lst: [c.strip() for c in lst] if lst and lst!=[''] else [])\n",
    "\n",
    "#Check if there is duplicated rows\n",
    "print(f\"Number of duplicate rows: {df.duplicated().sum()}\")\n",
    "\n",
    "df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')\n",
    "df['year_added'] = df['date_added'].dt.year\n",
    "\n",
    "#Save cleaned data\n",
    "df.to_csv(\"netflix-plotting/data/clean/netflix_clean.csv\", index=False)\n",
    "print(\"Saved cleaned to netflix-plotting/data/clean/netflix_clean.csv\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 85,
   "id": "90e53677-f41b-453b-a36a-e5041d652efd",
   "metadata": {},
   "outputs": [],
   "source": [
    "import os\n",
    "os.makedirs(\"netflix-plotting/outputs/figures\", exist_ok=True)\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
