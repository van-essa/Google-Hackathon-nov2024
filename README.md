# **AI-Powered Employee Scheduling System**

#### **Description**
This repository contains the development of an AI-powered employee scheduling system leveraging **Gemini AI** and **Google OR-Tools**. The project addresses the challenges of time-consuming and inefficient manual scheduling processes faced by managers in industries like manufacturing, retail, and hospitality. 

#### **Problem Statement**
Managers often struggle to create schedules that balance employee satisfaction and operational efficiency. The schedules frequently:
- Fail to account for essential employee preferences and constraints.
- Misalign with fluctuating business demands.
- Result in decreased productivity and employee dissatisfaction.

#### **Solution**
This AI-driven scheduling system aims to:
- Automatically generate optimized schedules that maximize operational efficiency while respecting employee needs.
- Reduce the time managers spend on scheduling tasks.
- Enhance employee satisfaction by incorporating flexibility and fairness into the process.

#### **Target Audience**
This system is designed for industries that rely heavily on effective workforce management:
- **Manufacturing**
- **Retail**
- **Hospitality**

#### **Technologies Used**
- **Gemini AI**: For predictive insights and employee satisfaction modeling.
- **Google OR-Tools**: For solving complex optimization problems to generate the best schedules.
- **Python**: As the core programming language.

#### **Project Goals**
1. Integrate predictive analytics to forecast workforce demands.
2. Implement optimization algorithms to align employee preferences with business goals.
3. Deliver an intuitive interface for managers to review and adjust schedules.

#### **Get Started**
Explore the repository for code, documentation, and guidelines to contribute to or utilize this innovative scheduling solution.

#### **Features Used for Prediction**
The model uses various features (input data) to make this prediction. In your case, the features might include:

- **Sick History:** How many sick days the employee has taken in the past (this could indicate whether they are likely to be sick again).
- **Seasonality:** Whether it is the flu season or a period of high illness (e.g., winter months like December and January).
- **Shift Info:** The type of work shift (e.g., Morning, Afternoon, or Night) the employee is scheduled for. Shifts may influence an employee’s risk of becoming ill (e.g., night shifts might be more stressful or cause more fatigue).
- **Location:** The geographical location where the employee works (which could have a seasonal flu outbreak).
- **Skill:** The type of work the employee does, which could be linked to stress or health risks.
- **Labor Compliance:** Whether the employee is compliant with labor laws (e.g., rest periods, working hours), which might influence health outcomes.

**How the Model Predicts:**
Given a set of these features for an employee on a specific day (like in your new_data example), the model will output a prediction of whether the employee is likely to be sick (1) or available (0).

For example, if you provide the model with the following data:

`new_data = pd.DataFrame({
    'Sick_History': [0.2],  # Past sick history (normalized)
    'Seasonality': [0],  # Off-peak season
    'Shift_Info_Afternoon': [0],  # Afternoon shift
    'Shift_Info_Night': [1],  # Night shift
    'Location_South': [1],  # Employee works in the South region
    'Skill_Maintenance': [0],  # Employee works in another skill category
    'Labor_Compliance': [1],  # Compliant with labor laws
})`

The model will look at these features and predict whether this employee is likely to be sick or available.
- **Output: **Prediction for new data: [1] means that the model predicts this employee is likely to be sick (1) on this day.
