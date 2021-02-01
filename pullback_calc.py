import pandas as pd




#these filters were found most effective from testing different combination in excel
#float is in millions
def pb_sqz_calculator(float, pm_volume, pm_range, open_price_retr) -> list:

    #import updated data
    play1_excel = pd.ExcelFile(r'Play1Data.xlsx')

    play1_df = pd.read_excel(play1_excel, 'Range Bound Play 1 (V2)-FLAT')
    pd.DataFrame(play1_df)
    play1_df.set_index(['Ticker', 'Date'], inplace = True)



    #drop NA values based on permarket hi input and sort by wins only

    win_filter = play1_df['W/L'] == 'W'
    play1_df = play1_df[win_filter]

    play1_df.dropna(axis = 0, inplace = True, subset = ['PM Hi'])





    #float filter
    if float == 0 or '':
        float_filter = play1_df['FLOAT(M)'] > -1
        float_filter1 = play1_df['FLOAT(M)'] > -1
    elif float < 50 and float > 0:
        float_filter = play1_df['FLOAT(M)'] <= 50
        float_filter1 = play1_df['FLOAT(M)'] > -1
    elif float > 50 and float < 100:
        float_filter = play1_df['FLOAT(M)'] > 50
        float_filter1 = play1_df['FLOAT(M)'] < 100
    else:
        float_filter = play1_df['FLOAT(M)'] >= 100
        float_filter1 = play1_df['FLOAT(M)'] >= 100
    #print(float_filter)

    #Pre market volume filter
    if pm_volume == 0 or '':
        pm_vol_filter = play1_df['PM VOL'] > -1
        pm_vol_filter1 = play1_df['PM VOL'] >-1
    elif pm_volume < 4000000 and pm_volume > 0:
        pm_vol_filter = play1_df['PM VOL'] <= 4000000
        pm_vol_filter1 = play1_df['PM VOL'] > -1
    elif pm_volume > 4000000 and pm_volume < 10000000:
        pm_vol_filter = play1_df['PM VOL'] >= 4000000
        pm_vol_filter1 = play1_df['PM VOL'] <= 10000000
    else:
        pm_vol_filter = play1_df['PM VOL'] >= 10000000
        pm_vol_filter1 = play1_df['PM VOL'] >= 10000000

    #Pre market range filter -- could just do basic filter based off of my input but that would give messy results - this is a cleaner solution for filters
    if pm_range == 0 or '':
        pm_range_filter = play1_df['Prior Close to PM Hi %'] > -1
        pm_range_filter1 = play1_df['Prior Close to PM Hi %'] > -1
    elif pm_range < .5 and pm_range > 0:
        pm_range_filter = play1_df['Prior Close to PM Hi %'] <= .5
        pm_range_filter = play1_df['Prior Close to PM Hi %'] > -1
    elif pm_range > .5 and pm_range < 1:
        pm_range_filter = play1_df['Prior Close to PM Hi %'] >= .5
        pm_range_filter = play1_df['Prior Close to PM Hi %'] <= 1
    else:
        pm_range_filter = play1_df['Prior Close to PM Hi %'] >= 1
        pm_range_filter1 = play1_df['Prior Close to PM Hi %'] >= 1



    #Retracement from pre market high to market open price
    if open_price_retr == 0 or '':
        op_ret_filter = play1_df['Opening Price % Retracement of Prior Move (relative to day)'] > -1
        op_ret_filter1 = play1_df['Opening Price % Retracement of Prior Move (relative to day)'] > -1
    elif open_price_retr < .2 and open_price_retr > 0:
        op_ret_filter = play1_df['Opening Price % Retracement of Prior Move (relative to day)'] <= .2
        op_ret_filter = play1_df['Opening Price % Retracement of Prior Move (relative to day)'] > -1
    elif open_price_retr > .2 and open_price_retr < .4:
        op_ret_filter = play1_df['Opening Price % Retracement of Prior Move (relative to day)'] >= .2
        op_ret_filter = play1_df['Opening Price % Retracement of Prior Move (relative to day)'] <= .4
    else:
        op_ret_filter = play1_df['Opening Price % Retracement of Prior Move (relative to day)'] >= .4
        op_ret_filter1 = play1_df['Opening Price % Retracement of Prior Move (relative to day)'] >= .4


    play1_df_filtered = play1_df[(float_filter) & (float_filter1) & (pm_vol_filter) & (pm_vol_filter1) & (pm_range_filter) & (pm_range_filter1) & (op_ret_filter) & (op_ret_filter)]


    #print(play1_df_filtered.shape)
    average_pullback = play1_df_filtered['Pullback % from open'].mean()
    average_squeeze = play1_df_filtered['Squeeze %'].mean()
    shape = play1_df_filtered.shape

    #0 spot will be for pullback and 1 spot will be for squeeze% in output list and 2 spot will be for number of samples in specefic test
    num_rows = shape[0]
    output_list = [average_pullback, average_squeeze, num_rows]
    print(output_list)
    return output_list


