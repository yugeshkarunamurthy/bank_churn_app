st.title("💴Bank Churn Prediction (Term Deposit Subscription)")
def user_input():
    age = st.slider("Age", 18, 95, 30)
    job = st.selectbox("Job", list(encoders['job'].classes_))
    marital = st.selectbox("Marital Status", list(encoders['marital'].classes_))
    education = st.selectbox("Education", list(encoders['education'].classes_))
    default = st.selectbox("Default Credit", list(encoders['default'].classes_))
    housing = st.selectbox("Housing Loan", list(encoders['housing'].classes_))
    loan = st.selectbox("Personal Loan", list(encoders['loan'].classes_))
    contact = st.selectbox("Contact", list(encoders['contact'].classes_))
    month = st.selectbox("Month", list(encoders['month'].classes_))
    day_of_week = st.selectbox("Day of Week", list(encoders['day_of_week'].classes_))
    duration = st.number_input("Call Duration (sec)", 0, 5000, 100)
    campaign = st.slider("Campaign", 1, 50, 1)
    pdays = st.slider("Pdays", -1, 999, 999)
    previous = st.slider("Previous Contacts", 0, 50, 0)
    poutcome = st.selectbox("Previous Outcome", list(encoders['poutcome'].classes_))
    emp_var_rate = st.slider("Employment Var Rate", -3.0, 2.0, 1.1)
    cons_price_idx = st.slider("Consumer Price Index", 90.0, 95.0, 93.0)
    cons_conf_idx = st.slider("Consumer Confidence Index", -50.0, 0.0, -40.0)
    euribor3m = st.slider("Euribor 3m", 0.0, 6.0, 4.0)
    nr_employed = st.slider("Number of Employed", 4000.0, 5500.0, 5000.0)

    data = {
        "age": age,
        "job": encoders["job"].transform([job])[0],
        "marital": encoders["marital"].transform([marital])[0],
        "education": encoders["education"].transform([education])[0],
        "default": encoders["default"].transform([default])[0],
        "housing": encoders["housing"].transform([housing])[0],
        "loan": encoders["loan"].transform([loan])[0],
        "contact": encoders["contact"].transform([contact])[0],
        "month": encoders["month"].transform([month])[0],
        "day_of_week": encoders["day_of_week"].transform([day_of_week])[0],
        "duration": duration,
        "campaign": campaign,
        "pdays": pdays,
        "previous": previous,
        "poutcome": encoders["poutcome"].transform([poutcome])[0],
        "emp.var.rate": emp_var_rate,
        "cons.price.idx": cons_price_idx,
        "cons.conf.idx": cons_conf_idx,
        "euribor3m": euribor3m,
        "nr.employed": nr_employed
    }

    return pd.DataFrame([data])

df_input = user_input()

if st.button("Predict"):
    X_scaled = scaler.transform(df_input)
    pred = model.predict(X_scaled)[0]
    st.success("✅ Will Subscribe!" if pred == 1 else "❌ Will Not Subscribe.")
