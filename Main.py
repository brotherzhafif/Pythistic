# EXAMPLE PROGRAM
import Chart as ct
import FrequencyTable as ft
import pandas as pd
import tabulate as tabulate
import Transform as tf

# Raw Data
dataset = [
    12.5, 12.5, 12.1, 12.6, 12.7, 12.5, 43.2, 43.2, 43.2, 43.5,
    34.2, 34.1, 34.3, 34.2, 34.0, 34.5, 56.7, 56.8, 56.5, 56.6,
    56.9, 57.0, 67.9, 67.8, 67.5, 67.6, 67.7, 78.4, 78.1, 78.3,
    78.2, 78.9, 78.8, 89.0, 89.1, 89.2, 90.5, 91.2, 90.3, 90.0,
    98.3, 98.1, 98.0, 99.5, 99.4, 99.6, 99.1, 99.2, 99.3, 99.0
]

# Initialize the chart object with common properties
chart = ct.Chart(title="Dataset Box Diagram", xlabel="Data", ylabel="Value")

data = ft.FrequencyTable(dataset)
data.PopulateSimple()
# Prepare a box diagram
chart.box(data.simple.frequency, data.simple.classval)

# Display the prepared chart
chart.show()

# Initialize the chart object with common properties
chart = ct.Chart(title="Dataset Box Diagram", xlabel="Data", ylabel="Value")

dataset_tf = tf.Transform(dataset).box_cox_transform()
data2 = ft.FrequencyTable(dataset_tf)
data2.PopulateSimple()
# Prepare a box diagram
chart.box(data2.simple.frequency, data2.simple.classval)

# Display the prepared chart
chart.show()

