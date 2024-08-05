# The Outfit Recommendation System
Overview: 

The Outfit Recommendation System is a machine learning-based application designed to suggest outfits based on user preferences, including gender, mood, weather, and occasion. The system utilizes a RandomForestClassifier to predict suitable outfits from a predefined dataset. Additionally, users can create a personalized wardrobe and get suggestions based on their selected items.

Features :

Outfit Suggestion: Provides outfit recommendations based on user inputs for gender, mood, weather, and occasion.
Wardrobe Creation: Allows users to create a custom wardrobe by selecting items from a list.
Wardrobe Display: Displays the user's custom wardrobe.
Wardrobe-Based Suggestion: Suggests outfits specifically from the user's custom wardrobe.

Libraries and Tools :

Pandas: For data manipulation and reading CSV files.
Scikit-Learn: For model training and prediction using RandomForestClassifier.
Tkinter: For creating the graphical user interface.
PIL (Pillow): For handling image display within the application.
NumPy: For numerical operations.
CSV: For reading and writing CSV files.

Project Structure :

dataset.csv: The main dataset containing various outfits and their corresponding categories.
updated-file.csv: A temporary file used to store filtered wardrobe data.
bbb.png: An image used in the application for aesthetic purposes.
final_outfit_recommendation.py: The main script containing all the logic for the outfit recommendation system.

Usage :

Run the Application: Execute the final_outfit_recommendation.py script to launch the GUI.
Input Preferences: Select your preferences for gender, mood, weather, and occasion.
Get Suggestions: Click the "Get Outfit Suggestion" button to receive an outfit recommendation.
Create Wardrobe: Open the wardrobe creation window, select items, and save them to your custom wardrobe.
Display Wardrobe: View the items in your custom wardrobe.
Wardrobe-Based Suggestion: Get outfit suggestions specifically from your custom wardrobe.

How It Works :

Data Preprocessing: The dataset is read from a CSV file and categorical variables are converted to numerical using one-hot encoding.
Model Training: The RandomForestClassifier is trained on the preprocessed data.
User Input Handling: User selections are converted to the same format as the training data.
Prediction: The trained model predicts an outfit based on user inputs.
Wardrobe Management: Users can create and manage a custom wardrobe, with suggestions based on selected items.
