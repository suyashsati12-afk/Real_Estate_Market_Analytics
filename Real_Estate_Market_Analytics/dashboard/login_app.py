import sys
import os

# ==============================
# Project & Data Paths
# ==============================

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")

# Add project root to Python path
sys.path.append(BASE_DIR)

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from auth.login import login_user
from auth.register import register_user
from dashboard.app_backup import show_dashboard


# ==============================
# Page Configuration
# ==============================

st.set_page_config(
    page_title="Real Estate Market Analytics",
    page_icon="🏠",
    layout="wide"
)


# ==============================
# Session State
# ==============================

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "username" not in st.session_state:
    st.session_state.username = ""


# ============================================================
# Dashboard After Login
# ============================================================

if st.session_state.logged_in:

    st.sidebar.title("🏠 Real Estate Analytics")
    st.sidebar.success(
        f"👋 Welcome, {st.session_state.username}"
    )

    page = st.sidebar.radio(
        "📌 Navigation",
        [
            "🏠 Dashboard",
            "📈 Price Prediction",
            "📊 Analytics",
            "📋 Dataset",
            "👤 Profile",
            "ℹ️ About"
        ]
    )

    # ==============================
    # Logout
    # ==============================

    if st.sidebar.button("🚪 Logout"):
        st.session_state.logged_in = False
        st.session_state.username = ""
        st.rerun()


    # ========================================================
    # Dashboard
    # ========================================================

    if page == "🏠 Dashboard":

        show_dashboard()


    # ========================================================
    # Price Prediction
    # ========================================================

    elif page == "📈 Price Prediction":

        st.title("📈 Price Prediction")

        file_path = os.path.join(
            DATA_DIR,
            "price_forecast.csv"
        )

        try:

            df = pd.read_csv(file_path)

            df["month"] = pd.to_datetime(
                df["month"]
            )

            st.subheader("Forecast Dataset")

            st.dataframe(
                df,
                use_container_width=True
            )

            fig, ax = plt.subplots(
                figsize=(10, 5)
            )

            ax.plot(
                df["month"],
                df["avg_price"],
                label="Actual Price",
                linewidth=2
            )

            ax.plot(
                df["month"],
                df["forecast_price"],
                label="Forecast Price",
                linewidth=2,
                linestyle="--"
            )

            ax.set_xlabel("Month")
            ax.set_ylabel("Price")

            ax.legend()

            plt.xticks(rotation=45)

            st.pyplot(fig)

        except FileNotFoundError:

            st.error(
                f"❌ File not found: {file_path}"
            )


    # ========================================================
    # Analytics
    # ========================================================

    elif page == "📊 Analytics":

        st.title("📊 Analytics Dashboard")

        file_path = os.path.join(
            DATA_DIR,
            "price_forecast.csv"
        )

        try:

            df = pd.read_csv(file_path)

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
                "📈 Average Property Price Trend"
            )

            fig, ax = plt.subplots(
                figsize=(10, 5)
            )

            ax.plot(
                df["month"],
                df["avg_price"],
                marker="o",
                linewidth=2
            )

            ax.set_xlabel("Month")
            ax.set_ylabel("Average Price")

            plt.xticks(rotation=45)

            st.pyplot(fig)

            # ==============================
            # Bar Chart
            # ==============================

            col1, col2 = st.columns(2)

            with col1:

                st.subheader(
                    "📊 Monthly Average Price"
                )

                chart = df.copy()

                chart["Month"] = (
                    chart["month"]
                    .dt.strftime("%b-%Y")
                )

                st.bar_chart(
                    chart.set_index("Month")[
                        "avg_price"
                    ]
                )


            # ==============================
            # Pie Chart
            # ==============================

            with col2:

                st.subheader(
                    "🥧 Price Comparison"
                )

                fig2, ax2 = plt.subplots(
                    figsize=(5, 5)
                )

                ax2.pie(
                    [
                        df["avg_price"].mean(),
                        df["forecast_price"].mean()
                    ],
                    labels=[
                        "Average",
                        "Forecast"
                    ],
                    autopct="%1.1f%%"
                )

                st.pyplot(fig2)


            # ==============================
            # Histogram
            # ==============================

            st.subheader(
                "📉 Price Distribution"
            )

            fig3, ax3 = plt.subplots(
                figsize=(10, 4)
            )

            ax3.hist(
                df["avg_price"],
                bins=10
            )

            ax3.set_xlabel("Price")
            ax3.set_ylabel("Frequency")

            st.pyplot(fig3)


            # ==============================
            # Statistical Summary
            # ==============================

            st.subheader(
                "📋 Statistical Summary"
            )

            st.dataframe(
                df.describe(),
                use_container_width=True
            )

        except FileNotFoundError:

            st.error(
                f"❌ File not found: {file_path}"
            )


    # ========================================================
    # Dataset Viewer
    # ========================================================

    elif page == "📋 Dataset":

        st.title("📋 Dataset Viewer")

        file = st.selectbox(
            "Select Dataset",
            [
                "price_forecast.csv",
                "price_history_clean.csv",
                "transactions.csv",
                "market_indicator.csv"
            ]
        )

        file_path = os.path.join(
            DATA_DIR,
            file
        )

        try:

            df = pd.read_csv(file_path)

            # ==============================
            # Search
            # ==============================

            search = st.text_input(
                "🔍 Search"
            )

            if search:

                df = df[
                    df.astype(str).apply(
                        lambda row:
                        row.str.contains(
                            search,
                            case=False,
                            na=False
                        ).any(),
                        axis=1
                    )
                ]


            # ==============================
            # Dataset Preview
            # ==============================

            st.subheader(
                "Dataset Preview"
            )

            st.dataframe(
                df,
                use_container_width=True
            )


            # ==============================
            # Download
            # ==============================

            st.download_button(
                label="⬇ Download CSV",
                data=df.to_csv(
                    index=False
                ),
                file_name=file,
                mime="text/csv"
            )


            # ==============================
            # Dataset KPIs
            # ==============================

            col1, col2 = st.columns(2)

            with col1:

                st.metric(
                    "Total Rows",
                    len(df)
                )

            with col2:

                st.metric(
                    "Total Columns",
                    len(df.columns)
                )


            # ==============================
            # Column Names
            # ==============================

            st.subheader(
                "📋 Column Names"
            )

            st.write(
                df.columns.tolist()
            )


            # ==============================
            # Summary
            # ==============================

            st.subheader(
                "📊 Dataset Summary"
            )

            st.dataframe(
                df.describe(
                    include="all"
                ),
                use_container_width=True
            )

        except FileNotFoundError:

            st.error(
                f"❌ File not found: {file_path}"
            )


    # ========================================================
    # Profile
    # ========================================================

    elif page == "👤 Profile":

        st.title("👤 User Profile")

        st.info(
            "User Information"
        )

        st.write(
            f"**Username:** "
            f"{st.session_state.username}"
        )

        st.write(
            "**Role:** Admin"
        )

        st.write(
            "**Project:** "
            "Real Estate Market Analytics"
        )

        st.write(
            "**Technology:** "
            "Python, Streamlit, Pandas, Matplotlib"
        )


    # ========================================================
    # About
    # ========================================================

    elif page == "ℹ️ About":

        st.title("ℹ️ About Project")

        st.markdown(
            """
# 🏠 Real Estate Market Analytics

This project predicts and analyzes real estate prices
using historical market data.

### 🔹 Technologies Used

- Python
- Streamlit
- Pandas
- Matplotlib
- SQLite

### 🔹 Features

- 🔐 Login & Registration
- 📊 Dashboard
- 📈 Price Prediction
- 📉 Analytics
- 📋 Dataset Viewer
- 👤 User Profile

### 🔹 Developed For

Final Year Data Science Project
"""
        )

    # Stop execution after dashboard
    st.stop()


# ============================================================
# Login / Register Page
# ============================================================

st.title("🏠 Real Estate Market Analytics")

menu = st.radio(
    "Select Option",
    ["Login", "Register"],
    horizontal=True
)

username = st.text_input(
    "Username"
)

password = st.text_input(
    "Password",
    type="password"
)


# ============================================================
# Register
# ============================================================

if menu == "Register":

    if st.button("Create Account"):

        if username == "" or password == "":

            st.warning(
                "Please fill all fields"
            )

        elif register_user(
            username,
            password
        ):

            st.success(
                "✅ Registration Successful"
            )

        else:

            st.error(
                "❌ Username already exists"
            )


# ============================================================
# Login
# ============================================================

else:

    if st.button("Login"):

        if username == "" or password == "":

            st.warning(
                "Please fill all fields"
            )

        elif login_user(
            username,
            password
        ):

            st.session_state.logged_in = True
            st.session_state.username = username

            st.rerun()

        else:

            st.error(
                "❌ Invalid Username or Password"
            )
           
