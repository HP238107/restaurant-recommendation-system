
# Restaurant Recommendation System

A recommendation model built in python which recommends restaurants to user based on their ratings. The project used a dataset available from the website kaggle the dataset consists og information about vendor, customer, order.

## Recommendation Model 
The model based on similarity score which is calculated using co-sine similarity. In this system cosine similarity was used to calculate sdistance between teo users to find similarity between two users and generate recommendation based on similarity.

## Working 
In the vend.py file we first load predicted score of ratings into user_final_ratings it can be considered as a critics for generating recommendations for users. To get recommendations from users we use the recommend function by passing the user id of the user for which we wish to get Recommendation. The function will return a list of recommendations of restaurants with their predicted rating by the user for that restaurant.
## Deployment

To deploy this code we will use stream lit and AWS for deployment


## Hi, I'm Priyanka! 👋

