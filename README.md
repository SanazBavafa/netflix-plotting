# 🎬 Netflix Plotting Project

This project is created to practice **Python + data visualization with Matplotlib**.  
The dataset is from Kaggle and contains information about Netflix movies and TV shows.

---

## 📂 Project Structure
netflix-plotting/
├─ data/
│ ├─ raw/ # raw dataset (not uploaded to GitHub)
│ └─ clean/ # cleaned dataset
├─ notebooks/ # Jupyter notebooks for interactive analysis
├─ scripts/ # Python scripts (e.g., clean_data.py)
├─ outputs/
│ └─ figures/ # generated plots and charts
├─ README.md # project description
├─ requirements.txt
├─ .gitignore

---

## ⚙️ Setup & Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/YOUR_USERNAME/netflix-plotting.git
   cd netflix-plotting
2. Create a virtual environment and install dependencies:
python -m venv venv
venv\Scripts\activate   # for Windows
pip install -r requirements.txt

🧹 Data Cleaning

To clean the raw dataset and save the output in data/clean/:

python scripts/clean_data.py

📊 Analysis & Visualization

Jupyter notebooks are located in notebooks/.

All plots will be saved in outputs/figures/.

Example output:

📦 Dependencies

The full list is in requirements.txt. Example:

pandas
matplotlib
seaborn
dateparser



📝 Notes

Raw data is not included in this repository due to size.

Download the dataset from Kaggle:
https://www.kaggle.com/shivamb/netflix-shows
