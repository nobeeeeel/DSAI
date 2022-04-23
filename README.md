# Welcome to the Stock-Analysis Repository
## About
This is a mini project for our SC1015 (Introduction to Data Science and Artificial Intelligence) module. In this project, we utilised the top 10 stocks from NASDAQ which we utilised from the Yahoo Finance API.
Within this repository, you will see the 2 code files, one for our linear regression and one for our QLearning bot.

## Contributors
1. Zhi Hao - Linear Regression, Data Cleaning and QLearning Bot
2. Nobel - QLearning Bot, Data Visualisation and Data Resampling
3. Tommy - Data Visualisation and Extraction

## Problem Definition
- How do stock prices fluctuate over time? Does it follow a fixed pattern that can be predicted over time?
- What model would be the best to predict stock prices and even make a decision on whether to buy or sell.

## Models Used
- QLearning Model Using TensorFlow
- Linear Regression using SKLearn

## What did we do
- We trained a QLearning bot using 20 years worth of data for the top 10 stocks in NASDAQ
- This bot will decide when to buy, sell or hold the stock over a given period of time and we will monitor its effetiveness by the returns obtained by the bot
- We then utilised a linear regression model on the same 10 stock prices and used it to predict future stock prices and decide whether to buy, hold or sell
- We then compared the returns of both the models to determine which is the better one

## Our Takeaways
Based on our findings, for this given period, the linear regression model actually outperformed the QLearning bot. However, we feel that the linear regression model and the QLearning Bot are for different uses. The QLearning Bot is actually more geared towards day trading as it uses historical data to predict the next day's prices and hence make a decision to buy sell or hold. The linear regression model on the other hand uses the whole set of data but is not able to predict future prices as accurately. It is more suited for long term investments as it can predict where the stock price is headed.

## References
