In the excel file there are multiple sheets, the Range Bound Play 1 (V2)-FLAT sheet contains cleans and refined data for this setup. You can feel free to ignore the (V1) of this as it is just the unfiltered and unrefined data for this setup.

In the excel file you will probably notice that quite a few values are left blank. If you sort by the W/L column all values that have UT and L purpesfully don't have data filled out. The ones that have W that are not filled out will be filled out soon. The UT and L valued columns will eventually have a few columns filled out for further analysis on losses.

W : Wins L : Losses UT: Untradeable

Wins are trades that fit criteria for this setup and moved upwards and hit my profit target. 

Losses are trades that fit criteria for this setup and moved downwards and hit my stop loss. 

Untradeable(s) are trades that fit technical criteria but had one or more major fundamental (or non-specifiable technical) faults, like large overhead supply, huge dilution (ATM or direct offering), gap down on open,etc. 


The reason that the data is not complete is because it is always changing. In any given week I may add or delete 20-50 data points depending on what my analysis is telling me to do. So to me the data is complete, it is just always a work in progress. 

Along with that, due to the speceficity of the data that is in the file it has been input manually by me. I am working on finding an API that will allow me more freedom in terms of accessing data at very specefic points and very specefic times. This is my next most important task, especially as my trading strategies change even more. 

But this is mainly why it is a slower process for inputting data and why there are lots of blank cells. 


I use this sheet as a guide, I will firsty go through and test different things within the sheet, like filtering out different combination. Then I will check my analysis page for basic things like averages, mins, maxs and std dev. I also do this with the linear reg model except I will just use the slope equation. Once I have either the equation or averages I need I will go through a large repository of data that I have collected in another excel file and backtest my new 'solution' to see if it works or not, then record my results. 




IMPORTANT NOTE ABOUT THE KMEANS Jupyter Notebook:  This notebook was made with the help of following a sigma coding tutorial, linked here https://www.youtube.com/watch?v=dhV8UWI1sjc&ab_channel=SigmaCoding . Please note that I adapted what was taught in the tutorial to fit my own data.
