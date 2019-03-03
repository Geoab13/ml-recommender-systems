# <p align="center"> Machine Learning Recommender Systems </p>
<p align="center"> George Aboalahad </p>

This repository contains short examples to grasp the concept of recommender systems with machine learning. There are several ways to make relevant recommendations to users, and in these examples only a for of the ways are demonstrated at a conceptual level.

## Popularity-Based Recommendations
This is one of the simplest ways to recommend items to users. It assumes that items that have been rated often by other users is popular and is therefor of interest to the user in question. Building on this assumption, popularity is measured by rating count for each item. Observe that popularity can be measured in other ways than this.

In the most central file *rating_final.csv*, the data is comprised of user ratings (Users) on restaurants called Places (Items). This information is complemented by the file *chefmozcuisine.csv* which contains further information about the cuisine that each restaurant serves. Not all restaurants are listed in the *chefmozcuisine.csv*.

## Correlation-Based Recommendations
This is another simple approach of recommending items to a user. In correlation-based recommendation systems items are recommended based on their correlation in user reviews. This approach takes into account user preferences by measuring the correlation of items' user reviews. Those items that users have rated similarily are recommended. The correlation is measured by the PearsonR correlation metric.

The data used in this example is the same as above but with an additional file, *geodata.csv*, containing the name of the restaurant in question.

## Classification-Based Recommendations
classification-based recommenders could are powered by a classification algorithm. In this demo we focus on using a simple neural network, logistic regression and random forrest tree model as a recommender. Classification-based recommenders are able to make personalized recommendations since they take into account user attributes, as well as purchase history and other contextual data. The idea with these recommenders is that they use previous data of users and known outcome (for instance a user subsribed to a membership or not), and finds patterns in these to be able to predict how new users will act. If we predict (with high confidence) that a new user will subscribe to a membership based on the user's attributes, we can personalize and direct an offer to this user.

In this example we have used the open-sourced bank marketing dataset available fo r download at the UCI Machine Learning Repository (https://archive.ics.uci.edu/ml/datasets/Bank+Marketing#). However, the specific dataset that comes with this repository have transormed some of the categorical data to dummy variables for conceptual demonstration purposes. Other variable transformation methods might be more suitable along with the inclusion of more descriptive variables.

The data is related with direct marketing campaigns (phone calls) of a Portuguese banking institution. The classification goal is to predict if the client will subscribe a term deposit (variable y).

It was originally created by: [Moro et al., 2014] S. Moro, P. Cortez and P. Rita. A Data-Driven Approach to Predict the Success of Bank Telemarketing. Decision Support Systems, Elsevier, 62:22-31, June 2014.

```
The accuracy of these classification models are very low. This is due to poor user data used in this example, along with no regards to model tuning. This example should hence only be used to grasp the concept of classification-based recommendation engines. ```
