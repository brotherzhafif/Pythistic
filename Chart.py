# Chart.py
import matplotlib.pyplot as plt
from matplotlib_venn import venn2, venn3

class Chart:
    def __init__(self, title="", xlabel="", ylabel=""):
        # Initialize the Chart class with common plotting properties.
        # title: The title of the chart.
        # xlabel: Label for the x-axis.
        # ylabel: Label for the y-axis.
        self.title = title
        self.xlabel = xlabel
        self.ylabel = ylabel
        self.figure = None  # Placeholder for the plot figure.

    def _apply_common_properties(self):
        # Apply common properties like title, xlabel, and ylabel to the current plot.
        if self.title:
            plt.title(self.title)
        if self.xlabel:
            plt.xlabel(self.xlabel)
        if self.ylabel:
            plt.ylabel(self.ylabel)

    def box(self, data):
        # Prepare a box diagram for visualizing the distribution of a dataset.
        self.figure = plt.figure(figsize=(10, 6))
        plt.boxplot(data)
        self._apply_common_properties()

    def pie(self, data, labels):
        # Prepare a pie chart to show percentage distribution.
        self.figure = plt.figure(figsize=(8, 8))
        plt.pie(data, labels=labels, autopct='%1.1f%%', startangle=140)
        if self.title:
            plt.title(self.title)

    def line(self, x_values, y_values):
        # Prepare a line chart to plot the relationship between x and y values.
        self.figure = plt.figure(figsize=(10, 6))
        plt.plot(x_values, y_values, marker='o')
        self._apply_common_properties()
        plt.grid()  # Display a grid for better readability.

    def histogram(self, data, bins=10):
        # Prepare a histogram for visualizing the distribution of a dataset.
        self.figure = plt.figure(figsize=(10, 6))
        plt.hist(data, bins=bins, alpha=0.7, color='b')
        self._apply_common_properties()

    def boxplot(self, data):
        # Prepare a boxplot using seaborn-like aesthetics for enhanced visualization.
        self.figure = plt.figure(figsize=(10, 6))
        plt.boxplot(data)
        self._apply_common_properties()

    def scatter(self, x_values, y_values):
        # Prepare a scatter plot to visualize the relationship between two variables.
        self.figure = plt.figure(figsize=(10, 6))
        plt.scatter(x_values, y_values, alpha=0.6, edgecolors='w', s=100)
        self._apply_common_properties()
        plt.grid()  # Display a grid for better readability.

    def heatmap(self, data, annot=True, cmap='viridis'):
        # Prepare a heatmap for visualizing a 2D matrix data.
        self.figure = plt.figure(figsize=(12, 8))
        plt.imshow(data, cmap=cmap, aspect='auto')
        if annot:
            for (i, j), val in np.ndenumerate(data):
                plt.text(j, i, f'{val}', ha='center', va='center', color='white')
        self._apply_common_properties()
        plt.colorbar()  # Show color scale.

    def venn(self, sets, set_labels):
        # Prepare a Venn diagram for visualizing the overlap between two or three sets.
        self.figure = plt.figure(figsize=(8, 8))
        if len(sets) == 2:
            venn2(sets, set_labels)
        elif len(sets) == 3:
            venn3(sets, set_labels)
        else:
            raise ValueError("Only 2 or 3 sets can be displayed in a Venn diagram.")
        if self.title:
            plt.title(self.title)

    def pareto(self, data, labels):
        # Prepare a Pareto chart with bars representing values and a line showing the cumulative percentage.
        # Sort data in descending order.
        sorted_data = sorted(zip(data, labels), reverse=True)
        data, labels = zip(*sorted_data)
        cumulative_percentage = [sum(data[:i + 1]) / sum(data) * 100 for i in range(len(data))]

        self.figure, ax1 = plt.subplots(figsize=(12, 8))
        ax1.bar(labels, data, color='b', alpha=0.6)
        ax1.set_xlabel(self.xlabel)
        ax1.set_ylabel(self.ylabel)

        # Plot cumulative percentage line.
        ax2 = ax1.twinx()
        ax2.plot(labels, cumulative_percentage, color='r', marker='D', linestyle='-', linewidth=2)
        ax2.set_ylabel('Cumulative Percentage')
        ax2.yaxis.set_major_formatter(plt.FuncFormatter(lambda y, _: f'{y:.0f}%'))

        if self.title:
            ax1.set_title(self.title)

    def show(self):
        # Display the prepared chart.
        if self.figure:
            plt.show()
        else:
            print("No chart has been prepared. Please call a chart method first.")
