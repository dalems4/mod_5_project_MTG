# mod_5_project_MTG

# Why should Wizards of the coast care how strong their Magic the Gathering cards color integrity is?


## Overview
Magic the Gathering, MTG, is a card game based around it's "Color Wheel" that separates cards into different
playstyles and flavors. These different playstyles appeal to different parts of the Magic the Gathering
playerbase.

My goal is to build a Machine Learning model that takes in card text data and give a percentage based guess
on how likely the card is one of the 6 colors of magic; White, Blue, Black, Red, Green, or Colorless.

## Data sourcing
Wizards of the coast has a great MTG API with a python wrapper. Making aquiring all the text data from the sets I wanted to give my NLP Machine Learning model a breeze.

## Data Cleaning
To make my first model I wanted to only look at single color cards so I removed multi-color cards from my data set. After that my data was pretty clean and all I needed to do was OneHotEncode the text data.

## Modeling
I ran the OneHotEncoded text data through sklearn's term frequecy-inverse document frequecy, TF-IDF, to develope my model.

## Evaluation
My model mis-classified Green cards the most often, only guessing 55% right, out of the 4 core sets I gave it. This hints at Green not having as clear a color idenity as the other colors though the game play portion of the card's text. On the other hand my basic model was the best at guessing colorless cards with a ~72% accuracy.

## Deployment
I can keep further developing this machine learning model and present it to WOTC to help with their card development process in making Magic cards' colors feel and play more distinctly. 
