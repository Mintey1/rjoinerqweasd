import json, os, time, cloudscraper, webbrowser, pyautogui, random, requests
from discord_webhook import DiscordWebhook, DiscordEmbed
from colored import fg, attr


info = '%s[INFO] %s' % (fg(3), attr(0))
error = '%s[ERROR] %s' % (fg(1), attr(0))
success = '%s[SUCCESS] %s' % (fg(12), attr(0))
done = '%s[DONE] %s' % (fg(2), attr(0))

os.system(f'title Rain Joiner By: Carter, Edited by Mintey#0001^')

a = "True"
if os.path.exists('config.json'):
  with open("config.json", "r") as config:
    config = json.load(config)
  storage = []
  scraper = cloudscraper.create_scraper()


  webhookurl = config['webhook']
  ping = config['webhook_ping']
  auth = config['authorization']
else:
  auth1 = input(info +"Your bloxflip authentification?: ")
  webhookurl1 = input(info +"Your discord webhook link (leave blank if none): ")
  webhook1 = input(info +"What message should webhook include when sending rain notification?: ")
  time.sleep(1)
  print(info +"Creating config file with these needed things")
  time.sleep(2)
  fp = open('config.json', 'w')
  fp.write('{')
  fp.write('  "authorization":'+ " " + '"' + auth1 + '"' + ",")
  fp.write('  "webhook":'+ " " + '"' + webhookurl1 + '"' + ",")
  fp.write('  "webhook_ping":'+ " " + '"' + webhook1 + '"')
  fp.write('}')
  fp.close()
  time.sleep(1)
  print(success +"Succesfully done, restart app")
  time.sleep(2)

webhook = DiscordWebhook(url=webhookurl, content=f"{ping}")


try:
  get = scraper.get("https://rest-bf.blox.land/user", headers = {"origin": "https://bloxflip.com", "x-auth-token": auth})
  info = get.json()['user']
  print(f"Loading..")
  time.sleep(1)
  print(f'Remember to join Carters Playground discord server https://discord.gg/6wUUy4Pbd6')
  time.sleep(1)
  print(success+ f"Currently Logged in as {info['robloxUsername']}\nCurrent balance: {info['wallet']}\n\n")
except:
  input(error+ "The Token You Provided Is Invalid\nPlease press enter to exit.")
  quit()
if a == "True":
  thumburl = (f"https://www.roblox.com/headshot-thumbnail/image?userId={info['robloxId']}&height=50&width=50&format=png")
  embed = DiscordEmbed(title=f"I'm in!", url="https://bloxflip.com", color=0x6635EA)
  embed.add_embed_field(name="Logged into bloxflip as", value=f"{info['robloxUsername']}")
  embed.add_embed_field(name="Your Current Robux", value=f"{info['wallet']}")
  embed.set_timestamp()
  embed.set_thumbnail(url=thumburl)
  webhook.add_embed(embed)
  webhook.execute()
  webhook.remove_embed(0)
        
while True:
    try:
      r = scraper.get('https://rest-bf.blox.land/chat/history').json()
      check = r['rain']
      if check['active'] == True:
          if check['prize'] >= 500:
            store = scraper.get("https://rest-bf.blox.land/user", headers = {"x-auth-token": f"{auth}"}).json()['user']['wallet']
            storage.append(store)
            grabprize = str(check['prize'])[:-2]
            prize = (format(int(grabprize),","))
            host = check['host']
            getduration = check['duration']
            convert = (getduration/(1000*60))%60
            duration = (int(convert))
            waiting = (convert*60+10)
            sent = time.strftime("%d/%m/%Y %H:%M:%S", time.localtime(int(time.time())))
            url = 'https://bloxflip.com'
            webbrowser.get().open(url, new=0, autoraise=True)
            time.sleep(1)
            while True:
              join = pyautogui.locateCenterOnScreen('pro.png', confidence = 0.7)
              if join:
                time.sleep(1)
                pyautogui.moveTo(join)
                time.sleep(0.5)
                pyautogui.click()
                time.sleep(waiting/3)
                pyautogui.hotkey('ctrl', 'w')
                break
            info = scraper.get("https://rest-bf.blox.land/user", headers = {"x-auth-token": f"{auth}"}).json()['user']
            checker = scraper.get("https://rest-bf.blox.land/chat/history").json()['rain']['players']
            if info['robloxId'] in checker:
              print(success+ f"Successfully joined rain!\nRain amount: {prize} R$\nExpiration: {duration} minutes\nHost: {host}\nTimestamp: {sent}\n\n")
              if a == "True":
                thumburl = (f"https://i.pinimg.com/originals/50/15/7f/50157f642817c455e2ed7028e6ad31a8.gif")
                embed = DiscordEmbed(title=f"Successfully joined a rain!", url="https://bloxflip.com", color=0x6635EA)
                embed.add_embed_field(name="Rain Amount", value=f"{prize} R$")
                embed.add_embed_field(name="Expiration", value=f"{duration} minutes")
                embed.add_embed_field(name="Your Current Robux", value=f"{info['wallet']}")
                embed.set_timestamp()
                embed.set_thumbnail(url=thumburl)
                webhook.add_embed(embed)
                webhook.execute()
                webhook.remove_embed(0)
            else:
              print(error+ f"Failed to join rain!\nAmount: {prize} R$\nExpiration: {duration} mins\nHost: {host}\nTime: {sent}\n\n")
              if a == "True":
                thumburl = (f"https://i.pinimg.com/originals/50/15/7f/50157f642817c455e2ed7028e6ad31a8.gif")
                embed = DiscordEmbed(title=f"Failed to join rain!", url="https://bloxflip.com", color=0xde1414)
                embed.add_embed_field(name="Amount", value=f"{prize} R$")
                embed.add_embed_field(name="Expiration", value=f"{duration} mins")
                embed.add_embed_field(name="Your Current Robux", value=f"{info['wallet']}")
                embed.set_timestamp()
                embed.set_thumbnail(url=thumburl)
                webhook.add_embed(embed)
                webhook.execute()
                webhook.remove_embed(0)
            time.sleep(waiting)
      elif check['active'] == False:
        time.sleep(20)
    except Exception as e:
      print(e)
      time.sleep(20)
      #-- Join button hash(incase somehow corrupted): VGhpcyB3YXMgbWFkZSBieSBDYXJ0ZXIgU2VydmljZXMgdW5kZXIgdGhlIGdpdGh1YiB1c2VyIEBhamJvMTExICAgQW55IG90aGVyIHJlcG8ncyBhcmUgc2tpZHMuICAgT25seSB0cnVzdCB1cy4gT3VyIGRpc2NvcmQgaXM6IGh0dHBzOi8vZGlzY29yZC5nZy9KaFB1a2o5cXNQCk91ciB3ZWJzaXRlIGFsd2F5cyBoYXMgYSB2YWxpZCBsaW5rIHdoZW4gb3VyIHNlcnZlciBpcyB1cDogaHR0cHM6Ly9kZWVwaW5zaWRleW91Z3RhNS53aXhzaXRlLmNvbS9teS1zaXRl
