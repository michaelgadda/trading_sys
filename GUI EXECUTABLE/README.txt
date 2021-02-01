This is a version of a basic GUI I use daily for my trading! However I typically use a version I have in excel for ease of data transfer. 

I created this mainly so that I can display a few different processes I use in the morning in a more manageable and understandable way! 

If you would like to use this first download the GUI EXECUTABLE folder.

Then to use it just click on the "Main.exe" application 
 
It will open up a cmd, you don't need to do anything, it is just loading. 

Once it opens you can first try the top left buttons "Get stock info" and "Remove Stock info" 
	
 	NOTE: if you spell the ticker wrong (like aaapl instead of aapl) it will not give you an output or warning, so if you do not get an output please check your spelling and try again. 
	
	Once you click Get stock Info you will be prompted to enter a stock symbol. 
	You may add up to 5 tickers before you are told to clear the frame. 
	
	The data that you are seeing is being pulled from finviz, while I could of just used the full table from finviz these data points are what I find most use of when trading. 

Now onto the Pullback and Squeeze Calculator: 

	This one can be a little bit fussy sometimes because it uses my data, and sometimes over filtering the data provides 0 samples. 
	
	For ease of use and realistic purposes my recommendation is to have these inputs (Only input 2-3 at any given times and 0 for the ones you choose to not have inputs for):			*all numbers need to be greater than 0
			- Float: input < 50 (choose a num less than 50)
			- pm_vol: input < 4000000 
			-pm_range: input < 1.0 (float)
			-Retracement from open: input < .4 (float)
					
		If no output is given, just input zeros for two areas and numbers for the other 2 and it should work fine. 


		If there is output the output that you are receiving means this:
			Pullback: This is the average expected pullback the stock will have from the opening price before the stock squeezes
				   (so if the stock opens at 100 and the average expected pullback price is 5%, then we should see a pullback to level around 95, usually within 					2 std)
						-knowing the average gives me a center to scale my position around and a area that I will place my stop.
			Squeeze%: This gives me an average percent the stock moves from the entry point to the top of the squeeze. 
	
	
	Please note: In other setups I may use a different methods to find my outputs. For example if I am able to find a regression equation with a high r^2 between two or more variables I will use the regression equation to find my output insstead of a basic average. For this specefic setup I backtested both a linear regression equation and the basic average and the basic average produced much better results than using the regression line. 
	
		
	
	

Now onto the Entry and Exit Calculator: 


	There is only one condition that will not let this work and that is if the Min Required Average Entry Price is the same as the Planned Stop out Price. (DIV/0 error)

	Other than that all numbers will work. 
	
	However for realistic purposes here are the numbers I recommend: 
		
		*all numbers need to be positive
		Min Required Average Entry Price: ANY NUMBER 

		Planned Exit: This number should be GREATER than the Min Required Average Entry Price

		Planned Stop out price: This number should be less than the Min Required Average Entry Price 
		
		Dollar Risk Amount: ANY NUMBER 



		The output gives us: 

			Est % gain: what percentage we expect our position to increase if it works 
			Estimated % loss: what percentage we expect our position to decrease if the trade doesnt work
			Max. Position size: tells us in $ how big our position will be 
			Estimated Dollar gain: Tells us how much money we will make if it works 
			Max. Shares: Tells us how many shares we should use
			R/R: Tells us if our risk reward makes sense, for ease of use I do reward to risk, so the higher the number the better it is. 
				For example if we have a plan that dictates we will make 150 if we win and lose 30 if we lose that would be a 5R setup. 
				
				
				
				


		
		
