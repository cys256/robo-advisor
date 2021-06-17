# robo-advisor


+ Use GitHub Desktop software to download or clone it onto your computer. Choose a familiar download location like the Desktop
+ Open the clone in Visual Studio Code
+ Creat an .env file in which you store your API key to issue requests from AlphaVantage API
+ In the .env file, create a variable so that your program reads the API key from this environment variable at run-time. The variable should read ALPHAVANTAGE_API_KEY="abc123"
+ If you do not have an API key from AlphaVantage API, visit “https://www.alphavantage.co/” and follow the instructions
+ In Terminal, create and activate a new Anaconda virtual environment using the following command-line instructions "conda create -n stocks-env python=3.8" and "conda activate stocks-env"
+ From within the virtual environment, install the required packages specified in the "requirements.txt" file you created using "pip install -r requirements.txt"
+ Execute the program using the command "python app/robo_advisor.py"
+ When prompted by the program, enter a valid stock ticker
+ The program will generate market data on the stock, a recommendation, and a reason for the recommendation.
+ Execute the program again using the command "python app/robo_advisor.py" if you would like to obtain the same information on another stock
+ Note: a local file named prices.csv will be generated in the data folder with the historical prices