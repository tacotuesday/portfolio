''' 
A PGN file is structured like this:

[Event "Let's Play!"]
[Site "Chess.com"]
[Date "2023.05.15"]
[Round "-"]
[White "pale_kings_blue"]
[Black "goodolchin"]
[Result "1-0"]
[CurrentPosition "rn2k3/pp2bB1p/2p3p1/8/8/BPNnR3/P1bP2PP/R5K1 b - - 0 18"]
[Timezone "UTC"]
[ECO "C42"]
[ECOUrl "https://www.chess.com/openings/Petrovs-Defense-Urusov-Lichtenhein-Defense"]
[UTCDate "2023.05.15"]
[UTCTime "11:19:14"]
[WhiteElo "412"]
[BlackElo "351"]
[TimeControl "1/86400"]
[Termination "pale_kings_blue won by resignation"]
[StartTime "11:19:14"]
[EndDate "2023.05.15"]
[EndTime "21:51:06"]
[Link "https://www.chess.com/game/daily/517294807"]
[WhiteUrl "https://images.chesscomfiles.com/uploads/v1/user/218806793.d538bbff.50x50o.d6ec7509963b.jpg"]
[WhiteCountry "2"]
[WhiteTitle ""]
[BlackUrl "https://images.chesscomfiles.com/uploads/v1/user/188202459.74f2b3ad.50x50o.1aa9ec67f652.jpeg"]
[BlackCountry "52"]
[BlackTitle ""]

1. e4 e5 2. Nf3 Nf6 3. Bc4 Nxe4 4. Nxe5 d5 5. Nxf7 Kxf7 6. Qf3+ Ke8 7. Qh5+ g6 8. Qxd5 Qxd5 9. Bxd5 Bf5 10. O-O c6 11. Bb3 Nc5 12. Re1+ Be7 13. Bc4 Bxc2 14. Nc3 Nd3 15. Re3 Rf8 16. b3 Rxf2 17. Ba3 Rf7 18. Bxf7+ 1-0 

Write a script to convert this into tabular data.'''

# Convert PGN to tabular format
# PGN is a text format for recording chess games.
