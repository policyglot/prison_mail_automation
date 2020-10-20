# prison_mail_automation
A prototype for identifying similar incoming email queries from prison inmates' families and automate common answers

We will be testing a number of classification algorithms, including the following:
- Logistic Regression
- Naives Bayes
- Support Vector Machines
We will then switch to deep learning approaches including:
- LSTM
- RNN

The final choice will be based on classification accuracy.

Thereafter this project shifts to Airflow to help automate the use of templates to reply to emails. 

This project also relies on Active Learning to help classify issues accurately. For this, we turn to the [excellent work by Dr. Robert Munro](https://github.com/rmunro/pytorch_active_learning). We will be building a basic User Interface to first classify messages into one or more of the following categories:
- HB94 Information
- IDOC
- Sentence Reduction
- Difficulties in Contacting
- Segregation
- Insufficient Health Measures/ Medical Facilities for COVID-19
- Denial of Information/ Debarred from Access to Law Library
- Lack of Hygiene
- Insufficient Nutrition or Poor Quality of Food
- Water, Sanitation and Cleanliness

