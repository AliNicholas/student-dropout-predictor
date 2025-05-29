import streamlit as st
import pandas as pd
import numpy as np
import joblib

# 1. Load pipeline (scaler + model)
pipe = joblib.load("model/dropout_predict_pipeline.joblib")

# 2. Page config
st.set_page_config(page_title="🎓 Student Dropout Predictor", layout="wide")
st.title("🎓 Student Dropout Predictor")
st.write("Masukkan nilai 20 fitur di form berikut, lalu klik **Predict**.")

# 3. Daftar fitur & opsi kategori numerik sesuai README
features = [
    "Curricular_units_2nd_sem_approved",
    "Curricular_units_2nd_sem_grade",
    "Curricular_units_1st_sem_grade",
    "Curricular_units_1st_sem_credited",
    "Curricular_units_1st_sem_approved",
    "Curricular_units_2nd_sem_credited",
    "Curricular_units_1st_sem_enrolled",
    "Curricular_units_1st_sem_evaluations",
    "Age_at_enrollment",
    "Application_mode",
    "Curricular_units_2nd_sem_enrolled",
    "Curricular_units_2nd_sem_evaluations",
    "Tuition_fees_up_to_date",
    "Marital_status",
    "Displaced",
    "Daytime_evening_attendance",
    "Application_order",
    "Gender",
    "Previous_qualification",
    "Scholarship_holder",
]

app_modes = [1, 2, 5, 7, 10, 15, 16, 17, 18, 26, 27, 39, 42, 43, 44, 51, 53, 57]
maritals = [1, 2, 3, 4, 5, 6]
attends = [1, 0]  # 1=Daytime, 0=Evening
genders = [1, 0]  # 1=Male,   0=Female
prev_q = [1, 2, 3, 4, 5, 6, 9, 10, 12, 14, 15, 19, 38, 39, 40, 42, 43]

# 4. Input form (4 rows x 5 cols)
inputs = {}
for row in range(4):
    cols = st.columns(5)
    for idx, col in enumerate(cols):
        feat_idx = row * 5 + idx
        if feat_idx >= len(features):
            break
        f = features[feat_idx]

        # Numeric float inputs
        if "grade" in f.lower() or "age" in f or f == "Application_order":
            if "grade" in f.lower():
                inputs[f] = col.number_input(f.replace("_", " ").title(), min_value=0.0, max_value=200.0, step=0.1, value=0.0)
            else:
                inputs[f] = col.number_input(f.replace("_", " ").title(), min_value=0, max_value=100, step=1, value=0)

        # Binary yes/no
        elif f in ["Tuition_fees_up_to_date", "Displaced", "Scholarship_holder"]:
            inputs[f] = col.selectbox(f.replace("_", " ").title(), options=[0, 1], format_func=lambda x: "No" if x == 0 else "Yes")

        # Categorical codes
        elif f == "Application_mode":
            inputs[f] = col.selectbox("Application Mode", options=app_modes, format_func=lambda x: str(x))
        elif f == "Marital_status":
            inputs[f] = col.selectbox(
                "Marital Status", options=maritals, format_func=lambda x: {1: "Single", 2: "Married", 3: "Widower", 4: "Divorced", 5: "Facto union", 6: "Legally separated"}[x]
            )
        elif f == "Daytime_evening_attendance":
            inputs[f] = col.selectbox("Attendance Mode", options=attends, format_func=lambda x: "Daytime" if x == 1 else "Evening")
        elif f == "Gender":
            inputs[f] = col.selectbox("Gender", options=genders, format_func=lambda x: "Male" if x == 1 else "Female")
        elif f == "Previous_qualification":
            inputs[f] = col.selectbox(
                "Previous Qualification",
                options=prev_q,
                format_func=lambda x: {
                    1: "Secondary",
                    2: "Bachelor's",
                    3: "Degree",
                    4: "Master's",
                    5: "Doctorate",
                    6: "Freq HE",
                    9: "12th inc.",
                    10: "11th inc.",
                    12: "Other-11th",
                    14: "10th yr",
                    15: "10th inc.",
                    19: "Basic ed 3rd",
                    38: "Basic ed 2nd",
                    39: "Tech spec",
                    40: "1st cycle",
                    42: "Prof tech",
                    43: "Master 2nd",
                }[x],
            )

        # Remaining are numeric integer
        else:
            inputs[f] = col.number_input(f.replace("_", " ").title(), min_value=0, step=1, value=0)

# 5. Predict button
if st.button("Predict"):
    # Buat DataFrame berkolom 'features'
    df_input = pd.DataFrame([[inputs[f] for f in features]], columns=features)

    # Predict
    probs = pipe.predict_proba(df_input)[0]
    pred = pipe.predict(df_input)[0]
    labels = pipe.named_steps["model"].classes_

    # Tampilkan
    st.subheader("🔍 Hasil Prediksi")
    outcome_text = "Graduate ✅" if pred == 1 else "Dropout ⚠️"
    st.markdown(f"**Outcome:** {outcome_text}")
    st.markdown(f"**Confidence:** {probs[pred]*100:.2f}%")
