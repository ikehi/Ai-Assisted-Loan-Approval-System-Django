# AI-Assisted Loan Approval System

![Fintech Edition](fin.png)

Welcome to the AI-Assisted Loan Approval System project! This repository contains the code and resources for a comprehensive loan management system developed as part of the HumanAize Hackathon Fintech Edition. The project leverages advanced AI techniques to streamline loan approval processes, aiming to enhance efficiency and accuracy in financial decision-making.

## Table of Contents
1. [Introduction](#introduction)
2. [Features](#features)
3. [Dataset](#dataset)
4. [Model](#model)
5. [Installation](#installation)
6. [Usage](#usage)
7. [Contributing](#contributing)
8. [Acknowledgements](#acknowledgements)

## Introduction
This project is designed to automate the loan approval process using an Artificial Neural Network (ANN) model. The system is built with Django, offering both client and server-side functionalities to manage and process loan applications efficiently. The ANN model achieves an impressive accuracy of around 96% in classifying loan approvals and rejections.

## Features
- **AI-Powered Loan Classification:** Utilizes a high-performance ANN model to predict loan approvals or rejections based on application data.
- **Django Framework:** Provides a robust and scalable web application framework for seamless client-server interactions.
- **User and Admin Dashboards:** Offers separate interfaces for loan applicants and administrators to manage applications and view predictions.
- **Scalable and Customizable:** Easily integrates with different datasets and scales to handle large volumes of loan applications.

## Dataset
The dataset used for training and testing the model is provided by YouData.ai. It includes various features related to loan applications, such as applicant demographics and financial information.

Link for The dataset : 

[https://www.youdata.ai/yourdata/669ccea99a7e184abf439505 ](https://datalink.youdata.ai/2p82bvue) 

## Model
The ANN model is trained to classify loan applications as either approved or rejected based on the provided dataset. The model is stored in an `.h5` file format for easy integration and deployment.

--the Model is Present in the Repository

## Installation
To set up the project locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/HARSHGit45/Ai-Assisted-Loan-Approval-System-Django
   cd ai-assisted-loan-approval-system-django
2. Install the required dependencies:
   ```bash
    pip install -r requirements.txt
3. Download the trained model and place it in the models directory
4. Download the Scaler model and place it in models directory

## Usage
To use the loan approval system, follow these steps:

1. **Run the Django development server:**
   ```bash
   python manage.py runserver

## Contributing
We welcome contributions from the community. If you have any ideas, suggestions, or bug reports, please open an issue or submit a pull request. For major changes, please discuss with us first.

## Acknowledgements
This project is developed in collaboration with YouData.ai. Special thanks to the Hack2skill Hackathon team for providing a platform to innovate and create impactful solutions.




  
