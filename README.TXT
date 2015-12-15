
            __               __             __
           /  )    _ _      (    '_ '_/_   /__)
          /(_/(//)(/(-()/) __)(//( /(/(-  / ( (//)
                  _/

 This is Dungeon Sucide Run: Twitter Edition.
 The objective of the game is to create a character and fight monsters and collect
 gold. There is no ability to heal so every fight brings your character closer to death.

 DSR:TE is a game played on Twitter. The game uses tweets as it's commandline. the way this fuctions is that a
 player tweets to the account using the @DunSuciRun tag. When the program spots this it runs the program based on the
 actions of the player. Currently, this game only has three options: Create new character,
 continue with current character or about.

 The 'About' option gives a brief synopsis of the game.

 Creating a new character creates a name, class and health for the character as well as a small amount of gold.
 When the character is created. If the player already possessed a character, they are given a new one. Once they created
 a new character they are brought to the dungeon select screen where they must pick the difficulty of the dungeon
 If the player selects 'continue' they are dungeon menu without creating a new character.

 The fight is only a single round. After the fight the character is given gold and the damage
 they sustain is removed from their health. Once a character's health is reduced to zero they are given a new character.

  DSR:TE uses a twitter API. Any time the game that requires input or text is outputted the method homeTimeline and
  printTweet in the twt_manager are called respectively.

  The Twitter API only allows 15 API calls every 15 minutes and going over will cause the system to time out for
  several minutes. Because of this limitation the game has has been set to only allow a call every 60 seconds.

  Text input brought in from homeTimeline is checked via the checkTweet in db_manager to confirm that the tweet does
  not exist. If the tweet exists the system will wait 60 seconds. If the tweet does not exist the game will then
  add the tweet to the database and proceed to return the text taken from the tweet.

  DSR:TE contains four databases: Dungeon, Monster, Character and Player. Dungeon and Monster are pre-seeded with a
  selection of pregenerated monsters and dungeons that create the setting for where player fights.
  Character contains data on the character such as name, user name and health. The Character Table is tied into the
  Player table which contains the players user name, message and date. This assures that any action taken by the player
  will only effect their own character.