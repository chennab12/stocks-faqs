"""Illustrative math; no prices, forecasts or individualized recommendations."""
def growth(initial, monthly, annual, years, fee=0):
    # Annual fee modeled multiplicatively; contributions at month-end.
    net=(1+annual)*(1-fee)-1
    rate=(1+net)**(1/12)-1
    value=initial
    series=[value]
    for _ in range(int(years*12)):
        value=value*(1+rate)+monthly
        series.append(value)
    return series

def required_monthly(initial,target,annual,years):
    n=int(years*12)
    r=(1+annual)**(1/12)-1
    factor=n if abs(r)<1e-12 else ((1+r)**n-1)/r
    return max(0,(target-initial*(1+r)**n)/factor)

def recovery(loss):
    return loss/(1-loss)

def weighted_return(weights,returns):
    return sum(w*r for w,r in zip(weights,returns))
