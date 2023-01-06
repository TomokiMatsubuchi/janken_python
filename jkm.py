import random

class Player():
  def hand(self): # 第一引数は自インスタンス(self)
    print("数字を入力してください")
    print("0:グー, 1:チョキ, 2:パー")
    input_hand = int(input())
    while True:
      if input_hand == 0:
        return input_hand
      elif input_hand == 1:
        return input_hand
      elif input_hand == 2:
        return input_hand
      else:
        print("0~2の数字を入力してください")
        print("0:グー, 1:チョキ, 2:パー")
        input_hand = int(input())

class Enemy():
  def hand(self):
    return random.randint(0,2) #戻り値(return)のない関数の実行結果は「値None, タイプNoneType」になる。

class Janken():
  def pon(self, player_hand, enemy_hand):
    janken = ["グー", "チョキ", "パー"]
    print("相手の手は" + janken[enemy_hand] + "です。")
    if player_hand == enemy_hand:
      print("あいこ")
      return True
    elif (player_hand == 0 and enemy_hand == 1) or (player_hand == 1 and enemy_hand == 2) or (player_hand == 2 and enemy_hand == 0):
      print("あなたの勝ちです。")
      return False
    else:
      print("あなたの負けです。")
      return False

class GameStart():
  @classmethod
  def jankenpon(cls):
    player = Player()
    enemy = Enemy()
    janken = Janken()
    next_game = True
    while next_game:
      next_game = janken.pon(player.hand(), enemy.hand())


GameStart.jankenpon()
