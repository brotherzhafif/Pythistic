# Python Statistic Program 
> My Statistic Tools made with Python 

### Required
- Matplotlib

      pip install matplotlib
- Numpy

      pip install numpy

### Structure
- Program Structure

      + Main.py                [ Main execute file ]
      + Dataset.py             [ Place to put the Dataset ]
      + Frequency.py           [ Frequency Table Module ]
      + Chart.py               [ Chart Display Module ]

### Module
- Frequency.py Variables Description

      # Data Needed For Frequency Table
      amount = amount/length of data
      dataset = the dataset from Dataset.py
      lowest = minimum dataset value
      highest = maximum dataset value 
      ranges = amount dataset range 
      classes = amount of dataset class
      interval = amount of interval for each frequency
      base = frequency table bottom data start point
      top = frequency table top data stop point

      # Processed Frequency Table Data 
      data_lower = each bottom data limit of each dataset class
      data_upper = each top data limit of each dataset class
      data_frequency = frequency for each dataset class
      data_range = combination of data_lower and data_upper showing the data frequency range



###  How to run
- Clone This Repositry -> Pythistic Folder

      git clone https://github.com/brotherzhafif/Pythistic.git
      cd Pythistic
- Open Dataset.py -> paste your 1D array data

      # Example 
      data = (1,3,6,8,4)
- Run the Main.py

      python Main.py       # for universal python distribution
      python3 Main.py      # for Python 3 distribution

### Author
    BrotherZhafif
