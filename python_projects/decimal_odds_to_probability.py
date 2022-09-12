# converts odds to implied probability percentage.
def implied_probability( home, draw, away):
    # calculates actual percentage of each odd.
    inverse_total = (1/home + 1/draw + 1/away)
    home_per = round((1/home / inverse_total)  * 100 , 2)
    draw_per = round((1/draw / inverse_total)  * 100 , 2)
    away_per = round((1/away / inverse_total)  * 100 , 2)
    return f' HOME {home_per} %   DRAW {draw_per} %   AWAY {away_per} %'

#test data is provided to run the code
implied_probability = implied_probability(2.16, 3.8, 3)  
print(implied_probability)  
