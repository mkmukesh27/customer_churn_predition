import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
# import xgboost as xgb
from flask import Flask, request, render_template
import pickle

model = pickle.load(open('final_model.pkl', 'rb'))

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/prediction', methods=['GET', 'POST'])
def predict():
    if request.method == "POST":
        SeniorCitizen = int(request.form['SeniorCitizen'])
        MonthlyCharges = float(request.form['MonthlyCharges'])
        TotalCharges = float(request.form['TotalCharges'])
        gender = request.form['gender']
        Partner = request.form['Partner']
        Dependents = request.form['Dependents']
        PhoneService = request.form['PhoneService']
        MultipleLines = request.form['MultipleLines']
        InternetService = request.form['InternetService']
        OnlineSecurity = request.form['OnlineSecurity']
        OnlineBackup = request.form['OnlineBackup']
        DeviceProtection = request.form['DeviceProtection']
        TechSupport = request.form['TechSupport']
        StreamingTV = request.form['StreamingTV']
        StreamingMovies = request.form['StreamingMovies']
        Contract = request.form['Contract']
        PaperlessBilling = request.form['PaperlessBilling']
        PaymentMethod = request.form['PaymentMethod']
        tenure_group = request.form['tenure_group']


        #SeniorCitizen
        # gender
        if gender == "Male":
            gender_Male = 1
            gender_Female = 0
        else:
            gender_Male = 0
            gender_Female = 1

        # Partner
        if Partner == "Yse":
            Partner_Yes = 1
            Partner_No = 0
        else:
            Partner_Yes = 0
            Partner_No = 1

        # Dependents
        if Dependents == "Yse":
            Dependents_Yes = 1
            Dependents_No = 0
        else:
            Dependents_Yes = 0
            Dependents_No = 1

        # PhoneService
        if PhoneService == "Yse":
            PhoneService_Yes = 1
            PhoneService_No = 0
        else:
            PhoneService_Yes = 0
            PhoneService_No = 1

        # MultipleLines
        if MultipleLines == "Yse":
            MultipleLines_Yes = 1
            MultipleLines_No = 0
            MultipleLines_No_phone_service = 0
        elif MultipleLines == "No":
            MultipleLines_Yes = 0
            MultipleLines_No = 1
            MultipleLines_No_phone_service = 0
        else:
            MultipleLines_Yes = 0
            MultipleLines_No = 0
            MultipleLines_No_phone_service = 1

        # InternetService
        if InternetService == "DSL":
            InternetService_DSL = 1
            InternetService_Fiber_optic = 0
            InternetService_No = 0
        elif InternetService == "Fiber optic":
            InternetService_DSL = 0
            InternetService_Fiber_optic = 1
            InternetService_No = 0
        else:
            InternetService_DSL = 0
            InternetService_Fiber_optic = 0
            InternetService_No = 1

        # OnlineSecurity
        if OnlineSecurity == "Yse":
            OnlineSecurity_Yes = 1
            OnlineSecurity_No = 0
            OnlineSecurity_No_phone_service = 0
        elif OnlineSecurity == "No":
            OnlineSecurity_Yes = 0
            OnlineSecurity_No = 1
            OnlineSecurity_No_phone_service = 0
        else:
            OnlineSecurity_Yes = 0
            OnlineSecurity_No = 0
            OnlineSecurity_No_phone_service = 1

        # OnlineBackup
        if OnlineBackup == "Yse":
            OnlineBackup_Yes = 1
            OnlineBackup_No = 0
            OnlineBackup_No_phone_service = 0
        elif OnlineBackup == "No":
            OnlineBackup_Yes = 0
            OnlineBackup_No = 1
            OnlineBackup_No_phone_service = 0
        else:
            OnlineBackup_Yes = 0
            OnlineBackup_No = 0
            OnlineBackup_No_phone_service = 1

        # DeviceProtection
        if DeviceProtection == "Yse":
            DeviceProtection_Yes = 1
            DeviceProtection_No = 0
            DeviceProtection_No_phone_service = 0
        elif DeviceProtection == "No":
            DeviceProtection_Yes = 0
            DeviceProtection_No = 1
            DeviceProtection_No_phone_service = 0
        else:
            DeviceProtection_Yes = 0
            DeviceProtection_No = 0
            DeviceProtection_No_phone_service = 1

        # TechSupport
        if TechSupport == "Yse":
            TechSupport_Yes = 1
            TechSupport_No = 0
            TechSupport_No_phone_service = 0
        elif TechSupport == "No":
            TechSupport_Yes = 0
            TechSupport_No = 1
            TechSupport_No_phone_service = 0
        else:
            TechSupport_Yes = 0
            TechSupport_No = 0
            TechSupport_No_phone_service = 1

        # StreamingTV
        if StreamingTV == "Yse":
            StreamingTV_Yes = 1
            StreamingTV_No = 0
            StreamingTV_No_phone_service = 0
        elif StreamingTV == "No":
            StreamingTV_Yes = 0
            StreamingTV_No = 1
            StreamingTV_No_phone_service = 0
        else:
            StreamingTV_Yes = 0
            StreamingTV_No = 0
            StreamingTV_No_phone_service = 1

        # StreamingMovies
        if StreamingMovies == "Yse":
            StreamingMovies_Yes = 1
            StreamingMovies_No = 0
            StreamingMovies_No_phone_service = 0
        elif StreamingMovies == "No":
            StreamingMovies_Yes = 0
            StreamingMovies_No = 1
            StreamingMovies_No_phone_service = 0
        else:
            StreamingMovies_Yes = 0
            StreamingMovies_No = 0
            StreamingMovies_No_phone_service = 1

        # Contract
        if Contract == "Month-to-month":
            Contract_Month_to_month = 1
            Contract_One_year = 0
            Contract_Two_year = 0

        elif Contract == "One year":
            Contract_Month_to_month = 0
            Contract_One_year = 1
            Contract_Two_year = 0

        else:
            Contract_Month_to_month = 0
            Contract_One_year = 0
            Contract_Two_year = 1

        # PaperlessBilling
        if PaperlessBilling == "Yse":
            PaperlessBilling_Yes = 1
            PaperlessBilling_No = 0
        else:
            PaperlessBilling_Yes = 0
            PaperlessBilling_No = 1

        # PaymentMethod
        if PaymentMethod == "Bank transfer (automatic)":
            PaymentMethod_Bank_transfer_automatic = 1
            PaymentMethod_Credit_card_automatic = 0
            PaymentMethod_Electronic_check = 0
            PaymentMethod_Mailed_check = 0
        elif PaymentMethod == "Credit card (automatic)":
            PaymentMethod_Bank_transfer_automatic = 0
            PaymentMethod_Credit_card_automatic = 1
            PaymentMethod_Electronic_check = 0
            PaymentMethod_Mailed_check = 0
        elif PaymentMethod == "Electronic check":
            PaymentMethod_Bank_transfer_automatic = 0
            PaymentMethod_Credit_card_automatic = 0
            PaymentMethod_Electronic_check = 1
            PaymentMethod_Mailed_check = 0
        else:
            PaymentMethod_Bank_transfer_automatic = 0
            PaymentMethod_Credit_card_automatic = 0
            PaymentMethod_Electronic_check = 0
            PaymentMethod_Mailed_check = 1

        # tenure_group
        if tenure_group == "1":
            tenure_group_1_12 = 1
            tenure_group_13_24 = 0
            tenure_group_25_36 = 0
            tenure_group_37_48 = 0
            tenure_group_49_60 = 0
            tenure_group_61_72 = 0
        elif tenure_group == "2":
            tenure_group_1_12 = 0
            tenure_group_13_24 = 1
            tenure_group_25_36 = 0
            tenure_group_37_48 = 0
            tenure_group_49_60 = 0
            tenure_group_61_72 = 0
        elif tenure_group == "3":
            tenure_group_1_12 = 0
            tenure_group_13_24 = 0
            tenure_group_25_36 = 1
            tenure_group_37_48 = 0
            tenure_group_49_60 = 0
            tenure_group_61_72 = 0
        elif tenure_group == "4":
            tenure_group_1_12 = 0
            tenure_group_13_24 = 0
            tenure_group_25_36 = 0
            tenure_group_37_48 = 1
            tenure_group_49_60 = 0
            tenure_group_61_72 = 0
        elif tenure_group == "5":
            tenure_group_1_12 = 0
            tenure_group_13_24 = 0
            tenure_group_25_36 = 0
            tenure_group_37_48 = 0
            tenure_group_49_60 = 1
            tenure_group_61_72 = 0
        else:
            tenure_group_1_12 = 0
            tenure_group_13_24 = 0
            tenure_group_25_36 = 0
            tenure_group_37_48 = 0
            tenure_group_49_60 = 0
            tenure_group_61_72 = 1

        data = {'SeniorCitizen': [SeniorCitizen], 'MonthlyCharges': [MonthlyCharges], 'TotalCharges': [TotalCharges],
       'gender_Female': [gender_Female], 'gender_Male': [gender_Male], 'Partner_No': [Partner_No], 'Partner_Yes': [Partner_Yes],
       'Dependents_No': [Dependents_No], 'Dependents_Yes': [Dependents_Yes], 'PhoneService_No': [PhoneService_No],
       'PhoneService_Yes': [PhoneService_Yes], 'MultipleLines_No': [MultipleLines_No],
       'MultipleLines_No phone service': [MultipleLines_No_phone_service], 'MultipleLines_Yes': [MultipleLines_Yes],
       'InternetService_DSL': [InternetService_DSL], 'InternetService_Fiber optic': [InternetService_Fiber_optic],
       'InternetService_No': [InternetService_No], 'OnlineSecurity_No': [OnlineSecurity_No],
       'OnlineSecurity_No internet service': [OnlineSecurity_No_phone_service], 'OnlineSecurity_Yes': [OnlineSecurity_Yes],
       'OnlineBackup_No': [OnlineBackup_No], 'OnlineBackup_No internet service': [OnlineBackup_No_phone_service],
       'OnlineBackup_Yes': [OnlineBackup_Yes], 'DeviceProtection_No': [DeviceProtection_No],
       'DeviceProtection_No internet service': [DeviceProtection_No_phone_service], 'DeviceProtection_Yes': [DeviceProtection_Yes],
       'TechSupport_No': [TechSupport_No], 'TechSupport_No internet service': [TechSupport_No_phone_service], 'TechSupport_Yes': [TechSupport_Yes],
       'StreamingTV_No': [StreamingTV_No], 'StreamingTV_No internet service': [StreamingTV_No_phone_service], 'StreamingTV_Yes': [StreamingTV_Yes],
       'StreamingMovies_No': [StreamingMovies_No], 'StreamingMovies_No internet service': [StreamingMovies_No_phone_service],
       'StreamingMovies_Yes': [StreamingMovies_Yes], 'Contract_Month-to-month': [Contract_Month_to_month], 'Contract_One year': [Contract_One_year],
       'Contract_Two year': [Contract_Two_year], 'PaperlessBilling_No': [PaperlessBilling_No], 'PaperlessBilling_Yes': [PaperlessBilling_Yes],
       'PaymentMethod_Bank transfer (automatic)': [PaymentMethod_Bank_transfer_automatic],
       'PaymentMethod_Credit card (automatic)': [PaymentMethod_Credit_card_automatic],
       'PaymentMethod_Electronic check': [PaymentMethod_Electronic_check], 'PaymentMethod_Mailed check': [PaymentMethod_Mailed_check],
       'tenure_group_1 - 12': [tenure_group_1_12], 'tenure_group_13 - 24': [tenure_group_13_24], 'tenure_group_25 - 36': [tenure_group_25_36],
       'tenure_group_37 - 48': [tenure_group_37_48], 'tenure_group_49 - 60': [tenure_group_49_60], 'tenure_group_61 - 72': [tenure_group_61_72]}


        df = pd.DataFrame.from_dict(data)

        # cols = model.features_names
        # df = df[cols]

        # prediction = model.predict(df)
        # print(prediction)
        prediction = model.predict(df.tail(1))
        probablity = model.predict_proba(df.tail(1))[:,1]
        
        if prediction==1:
            o1 = "This customer is likely to be churned!!"
            o2 = "Confidence: {}".format(probablity*100)
        else:
            o1 = "This customer is likely to continue!!"
            o2 = "Confidence: {}".format(probablity*100)

        return render_template("prediction.html", output1=o1, output2=o2)

    else:
        return render_template("prediction.html")


if __name__ == "__main__":
    app.run()