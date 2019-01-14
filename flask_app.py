from flask import Flask
from flask import render_template
import requests
import  pprint

app = Flask(__name__)

@app.route('/<match_id>')
def hello_world(match_id):
    response = requests.get('https://api.steampowered.com/IDOTA2Match_570/GetLiveLeagueGames/v1/?key=214106CB2C8490743CEEADAFB9C96BBC')
    try:
        data = response.json()
    except:
        return '404'
    name = '404'
    res = list(data.get('result').get('games'))
    x = 0
    y=0
    direposx = []
    direposy = []
    radiantposx = []
    radiantposy = []
    heroesd = []
    heroesr = []
    rosh = 1
    for item in res:
        if str(match_id) == str(item.get('match_id')):
            rosh = int(item.get('scoreboard').get('roshan_respawn_timer'))
            playersd = list(item.get('scoreboard').get('dire').get('players'))
            playersr = list(item.get('scoreboard').get('radiant').get('players'))
            for player in playersd:
                heroesd.append('https://www.trackdota.com/static/heroes/png_o/32/' + str(player.get('hero_id')) + '.png')
                direposx.append(int(player.get('position_x'))/20)
                direposy.append(int(player.get('position_y'))/20 * -1)
            for player in playersr:
                heroesr.append('https://www.trackdota.com/static/heroes/png_o/32/' + str(player.get('hero_id')) + '.png')
                radiantposx.append(int(player.get('position_x'))/20)
                radiantposy.append(int(player.get('position_y'))/20 * -1)
            name = item.get('dire_team').get('team_name') + ': ' + str(item.get('scoreboard').get('dire').get('score')) + ' VS ' + item.get('radiant_team').get('team_name') + ': ' + str(item.get('scoreboard').get('radiant').get('score'))
    return render_template('index.html', name = name ,direy = direposy, direx = direposx, radiantx = radiantposx, radianty = radiantposy, heroesd = heroesd, heroesr = heroesr, match_id = match_id, rosh = rosh)

if __name__ == '__main__':
    app.run(debug=True, use_debugger=False, use_reloader=False, passthrough_errors=True)