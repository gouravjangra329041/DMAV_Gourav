import pandas as pd

from missing_barchart import plot_bar_missing
from missing_linechart import plot_line_missing
from missing_piechart import plot_pie_missing
from missing_stairchart import plot_stair_missing
from missing_histogramchart import plot_histogram
from missing_variables_dataset import missing_variables


def main():
    # Load dataset
    df = pd.read_csv("missing_dataset.csv")

    print("\n--- Dataset Preview ---\n")
    print(df.head())

    print("\n--- Dataset Info ---\n")
    print(df.info())

    # Missing values summary
    missing_variables(df)

    # Charts
    plot_bar_missing(df)
    plot_line_missing(df)
    plot_pie_missing(df)
    plot_stair_missing(df)

    # Histogram
    plot_histogram(df)


if __name__ == "__main__":
    main()