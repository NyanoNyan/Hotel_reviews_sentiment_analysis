# Hotel reviews prediction using Sentiment Analysis

- Hotel review dataset : https://www.kaggle.com/anu0012/hotel-review
- View live project: https://sentiment-prediction-review.herokuapp.com/

*Live project link may take a few seconds to load*

### Exploratory Data analysis

<img src="images/top_broswers_used.png" width="400">

- From the hotel review dataset, Firefox is shown to be the most popular browser for reviewers, where Edge and Google Chrome came 2nd and 3rd respectively.

<img src="images/top_device_used.png" width="400">

- Moving on towards the devices used by the reviewers. Desktop and Mobile were the most used device to write a review in, which makes sense and Tablet fell down to last place.

<img src="images/total_count_response_type.png" width="400">

- Towards the response type, this is where we will look at the review and their corresponding sentiment. The data has an abumdence of happy response type compared to not happy. Therefore, there is mismatch on data types. The model will probably be able to predict happy reviews for the hotel better compared to 
not happy. To combat this there might be a need to gather more data on not happy responce type. But for now, I will try it without this. There might be some accruracy loss due to the mismatch of data.

<img src="images/Words in a review.png" width="800">

- It seems that reviews that were given were generally very long, with around 40-80 words were the most in a review. This is similar to both the happy and not happy reviews.

