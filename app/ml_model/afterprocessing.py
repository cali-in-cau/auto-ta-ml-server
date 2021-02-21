def calculate_bull_bear(image_prediction_data):
    bull_bear = {}

    date = list(image_prediction_data.keys())
    date.sort()
    last_date = date[-1]
    
    recent_data = image_prediction_data[last_date]
    bull_prob, bear_prob = (0,0)
    
    for data in recent_data:
        if(data[0][-4:] == "BULL"):
            bull_prob += data[1]
        elif(data[0][-4:] == "BEAR"):
            bear_prob += data[1]
        else:
            pass

    stock = "bull"
    if bull_prob < bear_prob : stock = "bear"

    bull_bear["date"] = last_date
    bull_bear["stock"] = stock
    bull_bear["prob"] = [bull_prob, bear_prob]

    return bull_bear