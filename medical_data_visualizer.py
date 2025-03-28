# medical_data_visualizer.py

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

def draw_cat_plot():
    # Import data
    df = pd.read_csv("medical_examination.csv")

    # Add 'overweight' column
    df['overweight'] = (df['weight'] / ((df['height'] / 100) ** 2)).apply(lambda x: 1 if x > 25 else 0)

    # Normalize data for cholesterol and gluc
    df['cholesterol'] = df['cholesterol'].apply(lambda x: 1 if x > 1 else 0)
    df['gluc'] = df['gluc'].apply(lambda x: 1 if x > 1 else 0)

    # Create DataFrame for cat plot using pd.melt
    df_cat = pd.melt(
        df,
        id_vars=["cardio"],
        value_vars=["cholesterol", "gluc", "smoke", "alco", "active", "overweight"]
    )

    # Group and reformat the data to split it by cardio
    df_cat = df_cat.groupby(["cardio", "variable", "value"]).size().reset_index(name="total")

    # Draw the catplot
    plot = sns.catplot(
        x="variable",
        y="total",
        hue="value",
        col="cardio",
        kind="bar",
        data=df_cat
    )

    fig = plot.fig
    return fig

def draw_heat_map():
    # Import data
    df = pd.read_csv("medical_examination.csv")

    # Add 'overweight' column
    df['overweight'] = (df['weight'] / ((df['height'] / 100) ** 2)).apply(lambda x: 1 if x > 25 else 0)

    # Normalize data for cholesterol and gluc
    df['cholesterol'] = df['cholesterol'].apply(lambda x: 1 if x > 1 else 0)
    df['gluc'] = df['gluc'].apply(lambda x: 1 if x > 1 else 0)

    # Clean the data
    df_heat = df[
        (df['ap_lo'] <= df['ap_hi']) &
        (df['height'] >= df['height'].quantile(0.025)) &
        (df['height'] <= df['height'].quantile(0.975)) &
        (df['weight'] >= df['weight'].quantile(0.025)) &
        (df['weight'] <= df['weight'].quantile(0.975))
    ]

    # Calculate the correlation matrix
    corr = df_heat.corr()

    # Generate a mask for the upper triangle
    mask = np.triu(np.ones_like(corr, dtype=bool))

    # Set up the matplotlib figure
    fig, ax = plt.subplots(figsize=(12, 10))

    # Draw the heatmap
    sns.heatmap(
        corr,
        mask=mask,
        annot=True,
        fmt=".1f",
        center=0,
        square=True,
        linewidths=.5,
        cbar_kws={"shrink": .45, "format": '%.2f'}
    )

    return fig
