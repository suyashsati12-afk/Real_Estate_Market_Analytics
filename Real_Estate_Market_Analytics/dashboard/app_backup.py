import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os


# ==============================
# Project & Data Path
# ==============================

BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

DATA_DIR = os.path.join(
    BASE_DIR,
    "data"
)


# ==============================
# Dashboard Function
# ==============================

def show_dashboard():

    st.title(
        "🏠 Real Estate Market Analytics Dashboard"
    )

    # ==============================
    # Load Dataset
    # ==============================

    file_path = os.path.join(
        DATA_DIR,
        "price_forecast.csv"
    )

    try:

        df = pd.read_csv(file_path)

    except FileNotFoundError:

        st.error(
            f"❌ Dataset not found: {file_path}"
        )

        return

    df["month"] = pd.to_datetime(
        df["month"]
    )


    # ==============================
    # KPI Cards
    # ==============================

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Average Price",
        f"₹ {df['avg_price'].mean():,.0f}"
    )

    col2.metric(
        "Maximum Price",
        f"₹ {df['avg_price'].max():,.0f}"
    )

    col3.metric(
        "Minimum Price",
        f"₹ {df['avg_price'].min():,.0f}"
    )

    st.divider()


    # ==============================
    # Line Chart
    # ==============================

    st.subheader(
        "📈 Price Prediction Trend"
    )

    fig, ax = plt.subplots(
        figsize=(10, 4)
    )

    ax.plot(
        df["month"],
        df["avg_price"],
        marker="o",
        label="Actual Price"
    )

    ax.plot(
        df["month"],
        df["forecast_price"],
        marker="s",
        linestyle="--",
        label="Forecast Price"
    )

    ax.set_xlabel("Month")
    ax.set_ylabel("Price")

    ax.legend()

    plt.xticks(
        rotation=45
    )

    st.pyplot(fig)


    st.divider()


    # ==============================
    # Pie + Bar Chart
    # ==============================

    col1, col2 = st.columns(2)


    # ==============================
    # Pie Chart
    # ==============================

    with col1:

        st.subheader(
            "🥧 Price Distribution"
        )

        fig, ax = plt.subplots(
            figsize=(5, 5)
        )

        values = [
            df["avg_price"].mean(),
            df["forecast_price"].mean()
        ]

        labels = [
            "Average",
            "Forecast"
        ]

        ax.pie(
            values,
            labels=labels,
            autopct="%1.1f%%"
        )

        st.pyplot(fig)


    # ==============================
    # Bar Chart
    # ==============================

    with col2:

        st.subheader(
            "📊 Average Price by Month"
        )

        chart = df.copy()

        chart["Month"] = (
            chart["month"]
            .dt.strftime("%b-%Y")
        )

        st.bar_chart(
            chart.set_index(
                "Month"
            )["avg_price"]
        )


    st.divider()


    # ==============================
    # Dataset Preview
    # ==============================

    st.subheader(
        "📋 Dataset Preview"
    )

    st.dataframe(
        df.head(20),
        use_container_width=True
    )

    st.write(
        f"📄 Total Rows : {len(df)}"
    )

    st.write(
        f"📊 Total Columns : {len(df.columns)}"
    )


    st.divider()


    # ==============================
    # Recent Forecast
    # ==============================

    st.subheader(
        "🗓 Recent Forecast"
    )

    st.dataframe(
        df.tail(5),
        use_container_width=True
    )


    st.divider()


    # ==============================
    # Transaction Trend
    # ==============================

    if "txn_count" in df.columns:

        st.subheader(
            "📈 Transaction Trend"
        )

        fig, ax = plt.subplots(
            figsize=(10, 4)
        )

        ax.plot(
            df["month"],
            df["txn_count"],
            marker="o"
        )

        ax.set_xlabel(
            "Month"
        )

        ax.set_ylabel(
            "Transactions"
        )

        plt.xticks(
            rotation=45
        )

        st.pyplot(fig)


    # ==============================
    # Growth Analysis
    # ==============================

    if "yoy_growth_pct" in df.columns:

        st.subheader(
            "📉 Year-on-Year Growth"
        )

        fig, ax = plt.subplots(
            figsize=(10, 4)
        )

        ax.plot(
            df["month"],
            df["yoy_growth_pct"],
            marker="o"
        )

        ax.set_xlabel(
            "Month"
        )

        ax.set_ylabel(
            "Growth (%)"
        )

        plt.xticks(
            rotation=45
        )

        st.pyplot(fig)


# ==============================
# Standalone Execution
# ==============================

if __name__ == "__main__":

    st.set_page_config(
        page_title="Real Estate Analytics",
        page_icon="🏠",
        layout="wide"
    )

    show_dashboard()
