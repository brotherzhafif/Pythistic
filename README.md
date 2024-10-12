# Python Statistic Program 
> My Statistic Tools made with Python 

### Features
- Frequency Table ( Done )
- Descriptive Statistics ( Work in Progress )
- Display Chart ( Work in Progress )
- Data Transformation ( Coming Soon )

### Required
- Matplotlib

      pip install matplotlib

- Numpy

      pip install numpy

- Tabulate

      pip install tabulate

- Pandas

      pip install pandas

### Structure
- Program Structure

      + Main.py                [ Main Control file ]
      + FrequencyTable.py      [ Frequency Table Module ]
      + Chart.py               [ Chart Display Module ]

### Module
- FrequencyTable.py Variables Description

      # Raw Data Needed For Frequency Table
      dataset = sorted dataset from your main.py input
      amount = amount/length of data
      lowest = minimum dataset value
      highest = maximum dataset value 
      range = amount dataset range ( all dataset value ) 
      classes = amount of dataset class
      interval = amount of interval for each frequency
      base = frequency table bottom data start point
      top = frequency table top data stop point 

      # Processed Frequency Table Data
      data = the main class for processed data
      data.bottom = lowest value of each dataset class
      data.top = highest value of each dataset class
      data.bottom_limit = bottom limit of each class
      data.top_limit = top limit of each class
      data.midpoint = midpoint of each class      
      data.frequency = frequency for each dataset class
      data.range = combination of data.top and data.bottom  showing the data frequency range
      data.limit = data range bottom and top limit

      data.relative_frequency = total of class relative frequency
      data.bottom_cumulative_frequency = total of bottom cumulative frequency
      data.top_cumulative_frequency = total of top cumulative frequency


###  How to run
- Clone This Repositry -> Pythistic Folder

      git clone https://github.com/brotherzhafif/Pythistic.git
      cd Pythistic
  
- Open Main.py -> paste your 1D array data into data variable

      # Example 
      import FrequencyTable as ft

      data = (
        58, 67, 45, 89, 72, 60, 76, 93, 
        55, 48, 62, 85, 79, 56, 41, 90, 
        77, 54, 68, 82, 46, 73, 57, 92, 
        81, 53, 66, 74, 64, 52, 91, 78, 
        49, 87, 88, 50, 69, 84, 43, 65, 
        83, 70, 44, 61, 75, 80, 71, 63, 47,51)
      
      # Initiate Object From The Raw Data
      table = ft.FrequencyTable(data)
      
      # Processing Raw Data to Frequency Table
      table.Populate()
      
      # Print The Data
      print(table.data.ranges) 
      print(table.data.frequency)

- Run the Main.py

      python Main.py       # for universal python distribution
      python3 Main.py      # for Python 3 distribution

### Author
    BrotherZhafif
